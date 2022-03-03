#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from sensor_msgs.msg import JointState
joint_state = JointState()

joint_state.position = [0,0,0,0,0,0]

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':
    rospy.init_node('pub_ang')
    pub = rospy.Publisher('ArmJointState', JointState, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.loginfo('Start!!!')
    
    while not rospy.is_shutdown():
        char = getch()
        if(char == 'w'):
            joint_state.position[1] = joint_state.position[1] + 1
        elif(char == 's'):
            joint_state.position[1] = joint_state.position[1] - 1
        elif(char == 'x'):
            break
        pub.publish(joint_state)

        char = ""
        rate.sleep()
