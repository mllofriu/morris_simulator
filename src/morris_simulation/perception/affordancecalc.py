'''
Created on May 22, 2013

@author: mllofriu
'''
import rospy

from morris_simulation.geometry.euclid import Point, Line, Movement
from morris_simulation.geometry.triangle import Triangle
from visualization_msgs.msg import Marker, MarkerArray
import geometry_msgs.msg
from math import pi, sin, cos

class AffordanceCalc(object):
    '''
    classdocs
    '''
    aperture = pi / 6
    possibleAngles = [-aperture, 0, aperture] 
    lenght = .3
    
    def __init__(self):
        '''
        Constructor
        '''
        self.pubMarker = rospy.Publisher("/triangles",MarkerArray, queue_size=10)
        
    def calcAffordances(self, lines):
        # Calculate affordances by intersecting agains one triangle per affordance
        # make initial triangle
        o = Point(0, 0, 0)  
        # The triangle is a bit behind
        v1 = Point(cos(self.aperture / 2) * self.lenght, sin(self.aperture / 2) * self.lenght, 0)
        v2 = Point(cos(self.aperture / 2) * self.lenght, -sin(self.aperture / 2) * self.lenght, 0)        
        t = Triangle([o, v1, v2])
        
        # for each angle: transform the triangle and intersect it with all lines
        lBase = Line(o, Point(1, 0, 0)); 
        affordances = []
        markers = []
        i = 0
        for angle in self.possibleAngles:
            # reference transformation
            lTransform = Line(o, Point(cos(angle), sin(angle), 0))
            mov = Movement(lBase, lTransform)
            tMoved = t.moved(mov);
            
            #canMove = True
            # Empty lines means no affordance (too close to the wall to see a line
            canMove = len(lines) > 0
            j = 0
            while j < len(lines) and canMove:
                l = lines[j]
                p1 = l.points[0]
                p2 = l.points[1]
                canMove = canMove and not tMoved.containedOrIntersect(Point(p1.x, p1.y, p1.z), Point(p2.x, p2.y, p2.z))
#                 if not canMove:
#                     print "cant move to", angle
#                     print tMoved.vertices
#                     print p1
#                     print p2
                j += 1
            affordances.append(canMove)
            
            if canMove:
                color = 'b'
            else:
                color = 'r'
            geomPoints = [geometry_msgs.msg.Point(p.r[0], p.r[1], p.r[2]) for p in tMoved.vertices]
            geomPoints.append(geomPoints[0])
            markers.append(self.getLineStrip(geomPoints, i, rospy.Time.now(), color))
            i += 1
       
        for l in lines:
#            print "line", a
            markers.append(self.getLineStrip([l.points[0], l.points[1]], i, rospy.Time.now(), 'g'))
            i = i + 1 
            
        mArray = MarkerArray()
        mArray.markers = markers
        self.pubMarker.publish(mArray)
        
        return affordances 
    
    def getLineStrip(self, points, lId, stamp, color):
        linesM = Marker()
        linesM.header.frame_id = "robot"
        # Use the same timestamp as the image
        linesM.header.stamp = stamp
        linesM.ns = ""
        linesM.id = lId
        linesM.type = Marker.LINE_STRIP
        linesM.action = Marker.ADD;
        linesM.points = points
        linesM.pose.orientation.w = 1.0 
        linesM.scale.x = .01;
        linesM.scale.y = .01;   
        linesM.scale.z = .01;
        if color == 'r':
            linesM.color.r = 1.0;
        if color == 'b':
            linesM.color.b = 1.0;
        if color == 'g':
            linesM.color.g = 1.0;
        linesM.color.a = 1.0;
        linesM.lifetime = rospy.Duration(.10)
        return linesM
