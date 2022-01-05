#!usr/bin/env python
from math import pi, sqrt, acos

import subprocess
import time
import RPi.GPIO as GPIO
import urllib
#import httplib
import http.client as httplib
import minimalmodbus
import time
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1)  # (port(str),slave adresse) // port série de raspberry = ttyAMA0 // port usb = ttyUSB0
instrument2 = minimalmodbus.Instrument('/dev/ttyUSB0',2)  # (port,adresse modbus)  // port série de raspberry = ttyAMA0 // port usb = ttyUSB0

instrument.serial.baudrate = 250000 # Defaults
instrument.serial.bytesize = 8 # Defaults
instrument.serial.parity = serial.PARITY_NONE # Defaults
instrument.serial.stopbits = 1
instrument.serial.timeout = 1  # secondes
instrument.mode = minimalmodbus.MODE_RTU  # rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument.debug = False
instrument.serial.xonxoff = True
instrument.serial.rtscts = False
instrument.serial.dsrdtr = False
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

instrument2.serial.baudrate = 250000
instrument2.serial.bytesize = 8
instrument2.serial.parity = serial.PARITY_NONE
instrument2.serial.stopbits = 1
instrument2.serial.timeout = 1  # secondes
instrument2.mode = minimalmodbus.MODE_RTU  # rtu ou ascii // MODE_ASCII ou MODE_RTU
instrument2.debug = False
instrument2.serial.xonxoff = True
instrument2.serial.rtscts = False
instrument2.serial.dsrdtr = False

usb1_on = True
usb2_on = True

if instrument.debug == True:

    print(instrument)


while 1:
    if usb1_on == True:
        try:
            
            print("Registres ID 1 USB")

            #test_reg = instrument.read_register(1,0)
            #print(test_reg)
            
            test_reg = instrument.read_registers(0, 16,4,Ture)  # .read_registers(registers address, number for content , Modbus function code 3 or 4) 
            print(test_reg)

            #test_reg = instrument2.read_registers(0,2,3)
            #print(test_reg)

            #position = instrument.write_register(0x9900, 0, number_of_decimals=2,functioncode=16, signed=False)
            #print (position)
            
            time.sleep(0.05)


        except:
            print("error USB1 -----------------------")
            time.sleep(8)

    if usb2_on == True:
        try:
            print("Registres ID 2 USB")
            
            #test_reg = instrument.read_register(1,0)
            #print(test_reg)

            test_reg = instrument2.read_registers(0, 16,3)  # .read_registers(registers address, number for content , Modbus function code 3 or 4) 
            print(test_reg)

            #test_reg = instrument.read_registers(10,10,4)
            #print(test_reg)

            time.sleep(0.05)

        except:
            print("error usb 2 ------------------------------")
            time.sleep(8)
