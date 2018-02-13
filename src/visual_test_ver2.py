#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Vector3,TransformStamped
from tf import TransformBroadcaster,transformations
from flight_cont_ver1.msg import Drone
from visualization_msgs.msg import MarkerArray,Marker

rospy.init_node('visual_test_ver2')
broadcaster=TransformBroadcaster()
quatanion=np.empty((4, ),dtype=np.float64)
rotate90x=transformations.quaternion_from_euler(0,np.pi/2,0)
Arrows=MarkerArray()

ArrowFL=Marker()
ArrowFR=Marker()
ArrowRR=Marker()
ArrowRL=Marker()

ArrowFL.header.frame_id = "/base_link"
ArrowFL.type = ArrowFL.ARROW
ArrowFL.action = ArrowFL.ADD

ArrowFL.scale.y = 0.005
ArrowFL.scale.z = 0.005
ArrowFL.color.a = 1.0
ArrowFL.color.r = 1.0
ArrowFL.color.g = 1.0
ArrowFL.color.b = 0.0
ArrowFL.pose.orientation.x=rotate90x[0]
ArrowFL.pose.orientation.y=rotate90x[1]
ArrowFL.pose.orientation.z=rotate90x[2]
ArrowFL.pose.orientation.w=rotate90x[3]

ArrowFR.header.frame_id = "/base_link"
ArrowFR.type = ArrowFR.ARROW
ArrowFR.action = ArrowFR.ADD

ArrowFR.scale.y = 0.005
ArrowFR.scale.z = 0.005
ArrowFR.color.a = 1.0
ArrowFR.color.r = 1.0
ArrowFR.color.g = 1.0
ArrowFR.color.b = 0.0
ArrowFR.pose.orientation.x=rotate90x[0]
ArrowFR.pose.orientation.y=rotate90x[1]
ArrowFR.pose.orientation.z=rotate90x[2]
ArrowFR.pose.orientation.w=rotate90x[3]

ArrowRR.header.frame_id = "/base_link"
ArrowRR.type = ArrowRR.ARROW
ArrowRR.action = ArrowRR.ADD

ArrowRR.scale.y = 0.005
ArrowRR.scale.z = 0.005
ArrowRR.color.a = 1.0
ArrowRR.color.r = 1.0
ArrowRR.color.g = 1.0
ArrowRR.color.b = 0.0
ArrowRR.pose.orientation.x=rotate90x[0]
ArrowRR.pose.orientation.y=rotate90x[1]
ArrowRR.pose.orientation.z=rotate90x[2]
ArrowRR.pose.orientation.w=rotate90x[3]

ArrowRL.header.frame_id = "/base_link"
ArrowRL.type = ArrowRL.ARROW
ArrowRL.action = ArrowRL.ADD

ArrowRL.scale.y = 0.005
ArrowRL.scale.z = 0.005
ArrowRL.color.a = 1.0
ArrowRL.color.r = 1.0
ArrowRL.color.g = 1.0
ArrowRL.color.b = 0.0
ArrowRL.pose.orientation.x=rotate90x[0]
ArrowRL.pose.orientation.y=rotate90x[1]
ArrowRL.pose.orientation.z=rotate90x[2]
ArrowRL.pose.orientation.w=rotate90x[3]

ArrowFL.id=0
ArrowFR.id=1
ArrowRR.id=2
ArrowRL.id=3

ArrowFL.pose.position.x = 0.102
ArrowFL.pose.position.y = -0.102
ArrowFL.pose.position.z = 0 
ArrowFR.pose.position.x = 0.102
ArrowFR.pose.position.y = 0.102
ArrowFR.pose.position.z = 0 
ArrowRR.pose.position.x = -0.102
ArrowRR.pose.position.y = 0.102
ArrowRR.pose.position.z = 0 
ArrowRL.pose.position.x = -0.102
ArrowRL.pose.position.y = -0.102
ArrowRL.pose.position.z = 0 

#ArrowFL.scale.x=0.1
#ArrowFR.scale.x=0.2
#ArrowRR.scale.x=0.3
#ArrowRL.scale.x=0.4

Arrows.markers=[ArrowFL,ArrowFR,ArrowRR,ArrowRL]

def callback(msg):
    quatanion=transformations.quaternion_from_euler(-msg.Euler.z,-msg.Euler.y,msg.Euler.x+np.pi,'rzyx')
    Arrows.markers[0].scale.x = (msg.Inputs.FL-msg.Trottle/9)*4
    Arrows.markers[1].scale.x = (msg.Inputs.FR-msg.Trottle/9)*4
    Arrows.markers[2].scale.x = (msg.Inputs.RR-msg.Trottle/9)*4
    Arrows.markers[3].scale.x = (msg.Inputs.RL-msg.Trottle/9)*4
    broadcaster.sendTransform((0,0,0),quatanion,rospy.Time.now(),"base_link","world")
    pub.publish(Arrows)

sub=rospy.Subscriber('Datas',Drone,callback)
#pub = rospy.Publisher('Arrows',Arrows,queue_size=50)
pub = rospy.Publisher('Arrows',MarkerArray,queue_size=50)
rospy.spin()