#!/usr/bin/env python3
import minimalmodbus
import serial
import time

instrument1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2)  
instrument3 = minimalmodbus.Instrument('/dev/ttyUSB0', 3)  
instrument4 = minimalmodbus.Instrument('/dev/ttyUSB0', 4)  
instrument5 = minimalmodbus.Instrument('/dev/ttyUSB0', 5)  
instrument6 = minimalmodbus.Instrument('/dev/ttyUSB0', 6)  

usb1_on = True
usb2_on = True
usb3_on = True
usb4_on = True
usb5_on = True
usb6_on = True

while 1:

    if usb1_on == True:
        try:

            print("Registres ID 1 USB")
            read_number1 = instrument1.read_register(1, 0)  # Registernumber, number of decimals
            print('read_number1 = ' + str(read_number1))

            time.sleep(1)

        except :
            print("error USB1 -----------------------")
            time.sleep(1)
    
    if usb2_on == True:
        try:

            print("Registres ID 2 USB")
            read_number2 = instrument2.read_register(2, 0)  # Registernumber, number of decimals
            print('read_number2 = ' + str(read_number2))

            time.sleep(1)

        except :
            print("error USB2 -----------------------")
            time.sleep(1)

    if usb3_on == True:
        try:

            print("Registres ID 3 USB")
            read_number3 = instrument3.read_register(3, 0)  # Registernumber, number of decimals
            print('read_number3 = ' + str(read_number3))

            time.sleep(1)

        except :
            print("error USB3 -----------------------")
            time.sleep(1)
    
    if usb4_on == True:
        try:

            print("Registres ID 4 USB")
            read_number4 = instrument4.read_register(4, 0)  # Registernumber, number of decimals
            print('read_number4 = ' + str(read_number4))

            time.sleep(1)

        except :
            print("error USB4 -----------------------")
            time.sleep(1)

    if usb5_on == True:
        try:

            print("Registres ID 5 USB")
            read_number5 = instrument5.read_register(5, 0)  # Registernumber, number of decimals
            print('read_number5 = ' + str(read_number5))

            time.sleep(1)

        except :
            print("error USB5 -----------------------")
            time.sleep(1)

    if usb6_on == True:
        try:

            print("Registres ID 6 USB")
            read_number6 = instrument6.read_register(6, 0)  # Registernumber, number of decimals
            print('read_number6 = ' + str(read_number6))

            time.sleep(1)

        except :
            print("error USB6 -----------------------")
            time.sleep(1)