#!/usr/bin/env python3
import rospy
import time
import RPi.GPIO as GPIO
from encoder import Encoder
from pid import PID

GPIO.setmode(GPIO.BCM)
IN1 = 27
IN2 = 21
IN3 = 13
IN4 = 26

ENA = 4
ENB = 19

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

def valueChanged(value, direction):
    print("* New value: {}, Direction: {}".format(value, direction))

e1 = Encoder(12, 20,valueChanged)
pid_m1 = PID(1,0.1,0.01,2000)

try:
    while True:
      pid_m1.update(e1.getValue())
      print(" control signal ="+str(pid_m1.getSignal()))
      print(pid_m1.getSP())
      print(pid_m1.getPTerm())
      print(pid_m1.getITerm())
      print(pid_m1.getDTerm())
      #print(pid_m1.getprev_error())

      PWMB.ChangeDutyCycle(pid_m1.getSignal())
      #PWMB.ChangeDutyCycle(100)
      direct = pid_m1.getdirect()
      if direct == 1 :
         GPIO.output(IN4,GPIO.HIGH)
         GPIO.output(IN3,GPIO.LOW)
      elif direct == -1 :
         GPIO.output(IN3,GPIO.HIGH)
         GPIO.output(IN4,GPIO.LOW)
except Exception:
    pass
    #PWMB.ChangeDutyCycle(0)
    #GPIO.output(IN3,GPIO.LOW)
    #GPIO.output(IN4,GPIO.LOW)

GPIO.cleanup()