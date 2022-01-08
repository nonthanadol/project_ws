#!/usr/bin/env python3

import RPi.GPIO as GPIO

BUTTON_GPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        # Interupts type :  RISING: when the state goes from LOW to HIGH.
        #                   FALLING: when the state goes from HIGH to LOW.
        
        #GPIO.wait_for_edge(BUTTON_GPIO, GPIO.BOTH) #both RISING and FALLING
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING)
        if not GPIO.input(BUTTON_GPIO):
            print("Button pressed!")
        else:
            print("Button released!")   