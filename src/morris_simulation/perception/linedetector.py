#!/usr/bin/env python

'''
Created on Jan 17, 2013

@author: mllofriu
'''

import roslib; roslib.load_manifest('morris_simulation')  # @UnresolvedImport
import rospy  # @UnresolvedImport

from morris_simulation.msg import Line, Lines
from visualization_msgs.msg import  Marker, MarkerArray
from sensor_msgs.msg import Image, CameraInfo, PointCloud
from geometry_msgs.msg import Point32
#from cmvision.msg import Blob
from cv2 import *
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from morris_simulation.geometry import CoordTransformer
from tf import TransformListener
import math

class LineDetector(object):
    '''
    This class takes the raw image and detects tape lines on the floor. 
    The topic lines is then published with the detected lines. 
    '''

    pub = None
    bridge = None
    green = None
    camFrame = "/CameraBottom_frame"
    floorFrame = "/base_footprint"
    maxLen = 10
    coordTransf = None
    eps = 20 # pixel width of the discarding frame
    
    def __init__(self):
        rospy.init_node('lineDetector')
        
        self.bridge = CvBridge()
        
        # Wait for info from the camera before getting any line
        rospy.loginfo( "Line Detector: subscribing to info topic")
        rospy.Subscriber("camera_info", CameraInfo, self.getCamInfo)
        self.pubMarker = rospy.Publisher("/line_vis_markers",MarkerArray)
        self.pubLines = rospy.Publisher("/lines",Lines)
        
    def getCamInfo(self, camInfo):
        if self.coordTransf == None:
            # Creater transformer from camera
            tfList = TransformListener()
            rospy.loginfo('Started coord transformer with' + str(camInfo.P[0])+  str(camInfo.P[5]))
            self.coordTransf = CoordTransformer(camInfo.P[0], camInfo.P[5], camInfo.width, 
                                                camInfo.height, tfList, self.camFrame,
                                                self.floorFrame)
            
            # Save info for later
            self.camInfo = camInfo
            
            # Subscribe to actual images
            rospy.loginfo( "subscribing to image topic")
            rospy.Subscriber("image", Image, self.processImage)
            
        
    def processImage(self, rosImage):
        # Discard old images
        #rospy.loginfo( "times" + str(rosImage.header.stamp) +","+ str(rospy.Time.now()))
        if rospy.Time.now() - rosImage.header.stamp < rospy.Duration(0.5):
#            rospy.loginfo("Received image") 
            try:
               img = self.bridge.imgmsg_to_cv(rosImage, desired_encoding="passthrough")
            except CvBridgeError, e:
                print "Macana:", e
                
            img = np.asarray(img)
            
#            rangeFiltered = inRange(img, np.asarray([0,0,0]), np.asarray([200,100,100]))    
#            gaussian_blur = GaussianBlur(rangeFiltered,(201,201),10)
#            retval, thrs = threshold(gaussian_blur, 200, 255, THRESH_BINARY)
#            img =  bitwise_and(img, img, mask=thrs)
            #img = GaussianBlur(img,(5,5),10)
            canny = Canny(img, 100, 200)
            lines = HoughLinesP(canny, 1, cv.CV_PI/180, 30, minLineLength=50,maxLineGap=50)
            
#             rosImagespy.loginfo(lines)
#            rospy.loginfo("Processed Image") 
    #        if (lines != None):
    #            for l in lines[0]:
    #                #rospy.loginfo(l)
    #                line(img, (l[0], l[1]),(l[2],l[3]), cv.CV_RGB(255, 0, 0), 3, 8)
            if lines <> None:
                lines = lines[0]
                # discard lines within a frame of eps pixels
                eps = self.eps
                lines = [l for l in lines if l[0] > eps and l[0] < self.camInfo.width - eps 
                         and l[1] > eps and l[1] < self.camInfo.height - eps]
                
                lines, lineMarkers = self.transformLines(lines, rosImage.header.stamp)
#                rospy.loginfo("Transformed Points") 
                self.publishLines(lineMarkers,lines, rosImage.header.stamp)
#                rospy.loginfo("Marker published")  
            else:
                self.publishLines([],[],rosImage.header.stamp)
            rospy.sleep(.5)
        else:
            rospy.logdebug("Frame discarded")
    
    def publishLines(self, markerLines, lines, stamp):
        markerArray = MarkerArray()
        markerArray.markers = markerLines
        self.pubMarker.publish(markerArray);
        
        linesMsg = Lines()
        linesMsg.header.stamp = stamp
        linesMsg.lines = lines
        self.pubLines.publish(linesMsg)
         
    def transformLines(self, lines, stamp):
        lineMarkers = []
        linesFound = []
        mId = 0
        tLines = self.coordTransf.transformLines(lines, stamp)
#         rospy.loginfo(lines)
#        for line in lines[0]:
#            rospy.loginfo("Transforming Coordinates") 
#            x1 = self.coordTransf.calcPosFromImgCoords(line[0],line[1],stamp)
#            x2 = self.coordTransf.calcPosFromImgCoords(line[2],line[3],stamp)
#            rospy.loginfo("Coordinates Transformed") 
        for l in tLines:
#            print l
            lenght = math.sqrt(math.pow(l[0].x - l[1].x, 2)+math.pow(l[0].y - l[1].y, 2))
            if lenght< self.maxLen:
                linesFound.append(Line(l[0],l[1]))
                lineMarkers.append(self.getLineStrip(l, mId, stamp))
                mId += 1
        
        return linesFound, lineMarkers
                   
    def getLineStrip(self, points, lId, stamp):
        linesM = Marker()
        linesM.header.frame_id = self.floorFrame
        # Use the same timestamp as the image
        linesM.header.stamp = stamp
        linesM.ns = ""
        linesM.id = lId
        linesM.type = Marker.LINE_STRIP
        linesM.action = Marker.ADD;
        linesM.points = points
        linesM.pose.orientation.w = 1.0 
        linesM.scale.x = .05;
        linesM.scale.y = .05;   
        linesM.scale.z = .05;
        linesM.color.r = 1.0;
        linesM.color.g = 1.0;
        linesM.color.b = 1.0;
        linesM.color.a = 1.0;
        linesM.lifetime = rospy.Duration(1.0)
        return linesM
