#!/usr/bin/env python

import rospy
from flight_cont_ver1.msg import Drone
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker
from tf import transformations
 
rospy.init_node('visual_test_ver1')
topic = 'maker'

marker = Marker()
marker.header.frame_id = "/base_frame"
marker.type = marker.ARROW
marker.action = marker.ADD
marker.scale.x = 0.1
marker.scale.y = 0.01
marker.scale.z = 0.01
marker.color.a = 1.0
marker.color.r = 1.0
marker.color.g = 1.0
marker.color.b = 0.0
marker.pose.position.x = 0
marker.pose.position.y = 0 
marker.pose.position.z = 0 
P0=Point()
P=Point()
P0.x=2
P0.y=0
P0.z=0

#marker.points.append(P0)

def callback(msg):
    marker.pose.orientation= msg.Sensor.orientation
    #P.x=3
    #P.y=100
    #P.z=1
    #marker.points.append(P)
    pub.publish(marker)


sub=rospy.Subscriber('Datas',Drone,callback)
pub = rospy.Publisher(topic, Marker,queue_size=50)

rospy.spin()