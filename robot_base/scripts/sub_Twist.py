#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time

IN1 = 27
IN2 = 21
IN3 = 13
IN4 = 26

ENA = 4
ENB = 19


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)

PWMA = GPIO.PWM(ENA,200) #create a PWM instance: // GPIO.PWM(channal,frequence)
PWMB = GPIO.PWM(ENB,200)

PWMA.start(0) # start PWM where (..) is the duty cycle (0.0% <= dc <= 100.0%)
PWMB.start(0)

GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)

#speed = 50
differential = 0.5
duty_cycle = 100

def SetMotorLeft(vel):
    #vel = int(vel)
    print('SetMotorLeft = '+str(vel))
    if vel < 0:
      pwm = -int(duty_cycle * vel)
      if pwm > duty_cycle:
         pwm = duty_cycle
      print('PWMA = '+str(pwm))
      PWMA.ChangeDutyCycle(pwm)
      SetMotorMode("leftmotor", "backward")
    elif vel > 0:
      pwm = int(duty_cycle * vel)
      if pwm > duty_cycle:
         pwm = duty_cycle
      print('PWMA = '+str(pwm))
      PWMA.ChangeDutyCycle(pwm)
      SetMotorMode("leftmotor", "forward")

def SetMotorRight(vel):
    #vel = int(vel)
    print('SetMotorRight = '+str(vel))
    if vel < 0:
      pwm = -int(duty_cycle * vel)
      if pwm > duty_cycle:
         pwm = duty_cycle
      print('PWMB = '+str(pwm))
      PWMB.ChangeDutyCycle(pwm)
      SetMotorMode("rightmotor", "backward")
    elif vel > 0:
      pwm = int(duty_cycle * vel)
      if pwm > duty_cycle:
         pwm = duty_cycle
      print('PWMB = '+str(pwm))
      PWMB.ChangeDutyCycle(pwm)
      SetMotorMode("rightmotor", "forward")

def SetMotorMode(motor,direct):
    print('setMotorMode '+ motor +' '+ direct) 
    if motor == 'leftmotor':
        if direct == 'backward' :
            print('leftmotor backward')
            GPIO.output(IN1,GPIO.HIGH)
            GPIO.output(IN2,GPIO.LOW)
        elif direct == 'forward' :
            print('leftmotor forward')
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.HIGH)
    if motor == 'rightmotor':
        if direct == 'backward' :
            print('rightmotor  backward')
            GPIO.output(IN3,GPIO.HIGH)
            GPIO.output(IN4,GPIO.LOW)
   
        elif direct == 'forward' :
            print('rightmotor  forward')
            GPIO.output(IN3,GPIO.LOW)
            GPIO.output(IN4,GPIO.HIGH)
    #else:
     #   GPIO.output(IN1,GPIO.LOW)
      #  GPIO.output(IN2,GPIO.LOW)
       # GPIO.output(IN3,GPIO.LOW)
        #GPIO.output(IN4,GPIO.LOW)
def callback(twist):
    left_speed = twist.linear.x - twist.angular.z * differential 
    right_speed = twist.linear.x + twist.angular.z * differential 
    print('left_speed = '+str(left_speed)+' right_speed = '+str(right_speed))
    SetMotorLeft(left_speed)
    SetMotorRight(right_speed)

if __name__ == '__main__':
    print ("Starting motor node")
    rospy.init_node('motors')
    rospy.Subscriber('cmd_vel', Twist,callback)
    rospy.spin()