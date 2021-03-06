#!/usr/bin/env python

import rosbag
import os
import sys
import math
import re

if len(sys.argv) < 2:
	print "Usage:", sys.argv[0], "dirWithDataBags"
	exit(1)

directory = sys.argv[1]


# Print headers
print "\"knowndistance\"", "\"estdistance\""
filenames = os.listdir(directory)
for f in filenames:
	#print f
	bag = rosbag.Bag(directory+f)
	m = re.search("(\d+)mm", f)
	knownDist = int(m.group(1))/1000.

	# Calc distances
	for topic, msg, t in bag.read_messages():
		x = msg.pose.position.x
		y = msg.pose.position.y
		#d = math.sqrt(x**2 + y**2)
		d = x
		print knownDist, d
	
	bag.close()
