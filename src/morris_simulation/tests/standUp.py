#!/usr/bin/env python
'''Walk: Small example to make Nao walk'''
import sys
import time
from naoqi import ALProxy

'''
Created on Mar 7, 2013

@author: mllofriu
'''

class StandUp(object):
    '''
    classdocs
    '''


    def __init__(self):
        robotIP = "elvira"
        '''
        Constructor
        '''
        # Init proxies.
        try:
            motionProxy = ALProxy("ALMotion", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALMotion"
            print "Error was: ", e
    
        try:
            postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
        except Exception, e:
            print "Could not create proxy to ALRobotPosture"
            print "Error was: ", e
    
        # Set NAO in Stiffness On
        self.StiffnessOn(motionProxy)
    
        # Send NAO to Pose Init
        postureProxy.goToPosture("Stand", .5)
    
        names = "HeadPitch"
        angleLists = .2
        timeLists = .5
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
#        postureProxy.goToPosture("Stand", 4)
        #####################
        ## Enable arms control by Walk algorithm
        #####################
        #motionProxy.setWalkArmsEnabled(False, False)



    def StiffnessOn(self,proxy):
        # We use the "Body" name to signify the collection of all joints
#        pNames = "Body"
#        pStiffnessLists = 1.0
#        pTimeLists = 1.0
#        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        proxy.setSmartStiffnessEnabled(True)

if __name__ == "__main__":
    StandUp()


    