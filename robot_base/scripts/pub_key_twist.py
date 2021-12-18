#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from robot_base.msg import twist

velocity = twist()

target_vel_left = 0
target_vel_right = 0

MAX_LIN_VEL = 0.26
#MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
#ANG_VEL_STEP_SIZE = 0.1

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def printscreen():
	print('vel_left = '+ str(target_vel_left) + ' vel_right = ' + str(target_vel_right))

def CheckLinearLimitVelocity(vel):
	if vel < -MAX_LIN_VEL :
		vel = -MAX_LIN_VEL
	elif vel > MAX_LIN_VEL :
		vel = MAX_LIN_VEL
	else: vel = vel
	return vel

if __name__ == '__main__':
    rospy.init_node('pub_vel')
    pub = rospy.Publisher('cmd_vel', twist, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.loginfo('Start!!!')
     
    while not rospy.is_shutdown():
            char = getch()
            if(char == 'w'):
                target_vel_left = CheckLinearLimitVelocity(target_vel_left + LIN_VEL_STEP_SIZE )
                target_vel_right = CheckLinearLimitVelocity(target_vel_right + LIN_VEL_STEP_SIZE )
                print('forward')
            elif(char == 's'):
                target_vel_left = CheckLinearLimitVelocity(target_vel_left - LIN_VEL_STEP_SIZE )
                target_vel_right = CheckLinearLimitVelocity(target_vel_right - LIN_VEL_STEP_SIZE )
                print('backward')
            elif(char == 'a'):
                target_vel_left = CheckLinearLimitVelocity(target_vel_left + LIN_VEL_STEP_SIZE )
                target_vel_right = CheckLinearLimitVelocity(target_vel_right - LIN_VEL_STEP_SIZE )
                print('CW')
            elif(char == 'd'):
                target_vel_left = CheckLinearLimitVelocity(target_vel_left - LIN_VEL_STEP_SIZE )
                target_vel_right = CheckLinearLimitVelocity(target_vel_right + LIN_VEL_STEP_SIZE )
                print('CCW')
            elif(char == 'x'):
                target_vel_left = 0
                target_vel_right = 0
                print('Stop')
            else: break

            printscreen()
            char = ""
            velocity.vel_left = target_vel_left
            velocity.vel_right = target_vel_right

            pub.publish(velocity)

            rate.sleep()

