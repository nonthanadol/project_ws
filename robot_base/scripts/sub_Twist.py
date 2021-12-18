#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

#speed = 50
differential = 50

def callback(twist):
    left_speed = twist.linear.x - twist.angular.z * differential 
    right_speed = twist.linear.x + twist.angular.z * differential 
    print('left_speed = '+str(left_speed)+' right_speed = '+str(right_speed))
   

if __name__ == '__main__':
    print ("Starting motor node")
    rospy.init_node('motors')
    rospy.Subscriber('cmd_vel', Twist,callback)
    rospy.spin()