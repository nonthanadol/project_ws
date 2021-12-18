#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from geometry_msgs.msg import Twist

velocity = Twist()

target_lin_vel= 0
target_ang_vel= 0

MAX_LIN_VEL = 0.26
MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

e = """Communications Failed"""

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
	print('Lin_vel = '+ str(target_lin_vel) + ' Ang_vel = ' + str(target_ang_vel))

def CheckLinearLimitVelocity(vel):
	if vel < -MAX_LIN_VEL :
		vel = -MAX_LIN_VEL
	elif vel > MAX_LIN_VEL :
		vel = MAX_LIN_VEL
	else: vel = vel
	return vel

def CheckAngularLimitVelocity(vel):
    if vel < -MAX_ANG_VEL :
        vel = -MAX_ANG_VEL
    elif vel > MAX_ANG_VEL :
        vel = MAX_ANG_VEL
    else: vel = vel
    return vel

if __name__ == '__main__':
    rospy.init_node('pub_vel')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.loginfo('Start!!!')
    try:
        while not rospy.is_shutdown():
            char = getch()
            if(char == 'w'):
                target_lin_vel = CheckLinearLimitVelocity(target_lin_vel + LIN_VEL_STEP_SIZE )
                print('forward')
            elif(char == 's'):
                target_lin_vel = CheckLinearLimitVelocity(target_lin_vel - LIN_VEL_STEP_SIZE )
                print('backward')
            elif(char == 'a'):
                target_ang_vel = CheckAngularLimitVelocity(target_ang_vel + ANG_VEL_STEP_SIZE)
                print('CW')
            elif(char == 'd'):
                target_ang_vel = CheckAngularLimitVelocity(target_ang_vel - ANG_VEL_STEP_SIZE)
                print('CCW')
            elif(char == 'x'):
                target_lin_vel = 0
                target_ang_vel = 0
                print('Stop')
            else: 
                if char == 'q' :      
                    break

            printscreen()
            char = ""
            velocity.linear.x = target_lin_vel
            velocity.angular.z = target_ang_vel

            pub.publish(velocity)

            rate.sleep()
    except:
        print(e)

    finally:
        velocity = Twist()
        velocity.linear.x = 0.0; velocity.linear.y = 0.0; velocity.linear.z = 0.0
        velocity.angular.x = 0.0; velocity.angular.y = 0.0; velocity.angular.z = 0.0
        pub.publish(velocity)
