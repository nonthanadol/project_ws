#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
from robot_arm.msg import ArmJointState
import math

#global total_step
#global total_step    

arm_steps = ArmJointState()
total_step = ArmJointState()

stepsPerRevolution = [64000,36571,149973,6400,28000,6400] # pluse stepper per Rev output

global joint_status
joint_status = 0

global count 
count = 0

#cur_angle
#joint_step[6];
prev_angle = [0,0,0,0,0,0] 
init_angle = [0,0,0,0,0,0]
#total_steps = [0,0,0,0,0,0]


def cmd_cb(cmd_arm):
    global count
    global joint_status
    #global total_step
    print('cmd_arm.position[0] :: '+str(cmd_arm.position[0]))
    if count == 0 :
        print('count == 0')
        prev_angle[0] = cmd_arm.position[0]
        prev_angle[1] = cmd_arm.position[1]
        prev_angle[2] = cmd_arm.position[2]
        prev_angle[3] = cmd_arm.position[3]
        prev_angle[4] = cmd_arm.position[4]
        prev_angle[5] = cmd_arm.position[5]

        init_angle[0] = cmd_arm.position[0]
        init_angle[1] = cmd_arm.position[1]
        init_angle[2] = cmd_arm.position[2]
        init_angle[3] = cmd_arm.position[3]
        init_angle[4] = cmd_arm.position[4]
        init_angle[5] = cmd_arm.position[5]
    
    arm_steps.position1 = int((cmd_arm.position[0]-prev_angle[0])*stepsPerRevolution[0]/360) #(2*math.pi))
    arm_steps.position2 = int((cmd_arm.position[1]-prev_angle[1])*stepsPerRevolution[1]/360) #(2*math.pi))
    arm_steps.position3 = int((cmd_arm.position[2]-prev_angle[2])*stepsPerRevolution[2]/360) #(2*math.pi))
    arm_steps.position4 = int((cmd_arm.position[3]-prev_angle[3])*stepsPerRevolution[3]/360) #(2*math.pi))
    arm_steps.position5 = int((cmd_arm.position[4]-prev_angle[4])*stepsPerRevolution[4]/360) #(2*math.pi))
    arm_steps.position6 = int((cmd_arm.position[5]-prev_angle[5])*stepsPerRevolution[5]/360) #(2*math.pi))
    
    rospy.loginfo(' arm_steps.position1 = ' + str(arm_steps.position1))

    if(count != 0 ):
        prev_angle[0] = cmd_arm.position[0]
        prev_angle[1] = cmd_arm.position[1]
        prev_angle[2] = cmd_arm.position[2]
        prev_angle[3] = cmd_arm.position[3]
        prev_angle[4] = cmd_arm.position[4]
        prev_angle[5] = cmd_arm.position[5]

    total_step.position1 += arm_steps.position1
    total_step.position2 += arm_steps.position2
    total_step.position3 += arm_steps.position3
    total_step.position4 += arm_steps.position4
    total_step.position5 += arm_steps.position5
    total_step.position6 += arm_steps.position6
    
    rospy.loginfo('  total_step.position1 = ' + str(total_step.position1))

    joint_status = 1
    count=1
    print('joint_status cmd = '+str(joint_status))
    print('count cmd = '+str(count))

if __name__ == '__main__':
    rospy.init_node('ConvertToStep')
    rospy.loginfo('in main function ')

    pub = rospy.Publisher("/Joint_Steps", ArmJointState, queue_size = 10)
    rospy.Subscriber('Ang', JointState ,cmd_cb)
    
    rate = rospy.Rate(10)
    
    print('joint_status main = '+str(joint_status))
    print('count main = '+str(count))

    while not rospy.is_shutdown():
        print("while ")

        if(joint_status ==1):
            print('joint_status if while = '+str(joint_status))
            print('count if while = '+str(count))
            print('joint_status==1')
            joint_status = 0
            pub.publish(total_step)

            rospy.loginfo('Published to /Joint_Steps')
        #rospy.spin()
        rate.sleep()
    rospy.spin()