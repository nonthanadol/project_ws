import time
import RPi.GPIO as GPIO
from encoder import Encoder

#### Motor ####
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 27
IN2 = 21
IN3 = 13
IN4 = 26

ENA = 4
ENB = 19

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

#### Encoder ####
def valueChanged(value, direction):
    print("* New value: {}, Direction: {}".format(value, direction))
e1 = Encoder(12, 20,valueChanged)

#### PID ####
Kp=1
Ki=1
Kd=1
SetPoint=2000
prev_error = 0.0
PTerm = 0.0
ITerm = 0.0
DTerm = 0.0
prev_time = 0
feedback_value = 0

def setmotor(pwm,direct):
    PWMB.ChangeDutyCycle(pwm)
    #PWMB.ChangeDutyCycle(100)
    if direct == 1 :
        GPIO.output(IN4,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
    elif direct == -1 :
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
    #GPIO.cleanup()

while True:
    #### Calculate ####
    current_time = time.time()
    delta_time = current_time - prev_time
    prev_time = current_time

    error = SetPoint - feedback_value
    PTerm = error
    feedback_value = e1.getValue()

    ITerm = ITerm + error*delta_time
    
    delta_error = error - prev_error
    dedt = delta_error / delta_time
    DTerm = dedt
    
    U = (Kp * PTerm) + (Ki * ITerm) + (Kd * DTerm)
    pwm = abs(U)
    if pwm > 100:
        pwm =100

    direct = 1
    if U>0 :
        direct = -1

    prev_error = error
    print('dt ='+str(delta_time))
    print('error = '+str(error))
    print('U = ' + str(U))
    print('P = '+ str(PTerm))
    print('I = '+ str(ITerm))
    print('D = '+ str(DTerm))
    setmotor(pwm,direct)

