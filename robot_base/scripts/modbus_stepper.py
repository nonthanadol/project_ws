#!/usr/bin/env python3
import minimalmodbus
import serial
import time

instrument1 = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument2 = minimalmodbus.Instrument('/dev/ttyUSB0', 2)  # port name, slave address (in decimal)

usb1_on = True
usb2_on = True

while 1:
    if usb1_on == True:
        try:
            
            print("Registres ID 1 USB")

            read_number = instrument1.read_register(11, 0)  # Registernumber, number of decimals
            print('stepper number : '+str(read_number)) 

            read_pos = instrument1.read_register(3, 0)  # Registernumber, number of decimals
            print('current position : '+str(read_pos))

            ledstatus1 = input("Enter 0 or 1 to turn off or on the led : ")
            instrument1.write_register(1, int(ledstatus1), 0)  # Registernumber, value, number of decimals for storage

            readledstatus1 = instrument1.read_register(1, 0)  # Registernumber, number of decimals
            print(readledstatus1)
            
            time.sleep(1)


        except :
            print("error USB1 -----------------------")
            time.sleep(8)

    if usb2_on == True:
        try:
            print("Registres ID 2 USB")

            read_number = instrument2.read_register(12, 0)  # Registernumber, number of decimals
            print('stepper number : '+str(read_number)) 

            read_pos = instrument2.read_register(4, 0)  # Registernumber, number of decimals
            print('current position : '+str(read_pos))
            
            ledstatus2 = input("Enter 0 or 1 to turn off or on the led: ")
            instrument2.write_register(2, int(ledstatus2), 0)  # Registernumber, value, number of decimals for storage

            readledstatus2 = instrument2.read_register(2, 0)  # Registernumber, number of decimals
            print(readledstatus2)
            
            time.sleep(5)

        except :
            print("error usb 2 ------------------------------")
            time.sleep(8)
