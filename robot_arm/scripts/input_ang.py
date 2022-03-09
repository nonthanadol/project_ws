#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from sensor_msgs.msg import JointState
joint_state = JointState()

joint_state.position = [0,0,0,0,0,0]

if __name__ == '__main__':
    rospy.init_node('input_ang')
    pub = rospy.Publisher('Ang', JointState, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.loginfo('Start!!!')
    
    while not rospy.is_shutdown():
        joint_state.position[0] =int(input("Angle Joint1 :: "))
        joint_state.position[1] =int(input("Angle Joint2 :: "))
        joint_state.position[2] =int(input("Angle Joint3 :: "))
        joint_state.position[3] =int(input("Angle Joint4 :: "))
        joint_state.position[4] =int(input("Angle Joint5 :: "))
        joint_state.position[5] =int(input("Angle Joint6 :: "))
        pub.publish(joint_state)
        rate.sleep()
