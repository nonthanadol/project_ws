#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from sensor_msgs.msg import JointState
joint_state = JointState()

joint_state.position = [0,0,0,0,0,0]
step = 1
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
    print("######## Joint State ##########")
    print('joint_state.position[0] :: '+str(joint_state.position[0]))
    print('joint_state.position[1] :: '+str(joint_state.position[1]))
    print('joint_state.position[2] :: '+str(joint_state.position[2]))
    print('joint_state.position[3] :: '+str(joint_state.position[3]))
    print('joint_state.position[4] :: '+str(joint_state.position[4]))
    print('joint_state.position[5] :: '+str(joint_state.position[5])+"\n")

if __name__ == '__main__':
    rospy.init_node('pub_ang')
    pub = rospy.Publisher('Ang', JointState, queue_size = 10)
    rate = rospy.Rate(10)
    rospy.loginfo('Start!!!')
    
    while not rospy.is_shutdown():
        char = getch()
        
        #Joint1
        if(char == 'q'):
            joint_state.position[0] = joint_state.position[0] + step
            # print('joint_state.position[0] :: '+str(joint_state.position[0]))
            printscreen()
        elif(char == 'a'):
            joint_state.position[0] = joint_state.position[0] - step
            #print('joint_state.position[0] :: '+str(joint_state.position[0]))
            printscreen()
        
        #Joint2 
        elif(char == 'w'):
            joint_state.position[1] = joint_state.position[1] + step
            # print('joint_state.position[1] :: '+str(joint_state.position[1]))
            printscreen()
        elif(char == 's'):
            joint_state.position[1] = joint_state.position[1] - step
            # print('joint_state.position[1] :: '+str(joint_state.position[1]))
            printscreen()
        
        #Joint3
        elif(char == 'e'):
            joint_state.position[2] = joint_state.position[2] + step
            # print('joint_state.position[2] :: '+str(joint_state.position[2]))
            printscreen()
        elif(char == 'd'):
            joint_state.position[2] = joint_state.position[2] - step
            # print('joint_state.position[2] :: '+str(joint_state.position[2]))
            printscreen()

        #Joint4
        elif(char == 'r'):
            joint_state.position[3] = joint_state.position[3] + step
            # print('joint_state.position[3] :: '+str(joint_state.position[3]))
            printscreen()
        elif(char == 'f'):
            joint_state.position[3] = joint_state.position[3] - step
            # print('joint_state.position[3] :: '+str(joint_state.position[3]))
            printscreen()

        #Joint5
        elif(char == 't'):
            joint_state.position[4] = joint_state.position[4] + step
            # print('joint_state.position[4] :: '+str(joint_state.position[4]))
            printscreen()
        elif(char == 'g'):
            joint_state.position[4] = joint_state.position[4] - step
            # print('joint_state.position[4] :: '+str(joint_state.position[4]))
            printscreen()

        #Joint6
        elif(char == 'y'):
            joint_state.position[5] = joint_state.position[5] + step
            # print('joint_state.position[5] :: '+str(joint_state.position[5]))
            printscreen()
        elif(char == 'h'):
            joint_state.position[5] = joint_state.position[5] - step
            # print('joint_state.position[5] :: '+str(joint_state.position[5]))
            printscreen()

        elif(char == 'x'):
            break

        pub.publish(joint_state)

        char = ""
        rate.sleep()
