#include <ModbusRtu.h>
#include <AccelStepper.h>
// assign the Arduino pin that must be connected to RE-DE RS485 transceiver
#define TXEN  2 

// data array for modbus network sharing
uint16_t au16data[16] = {
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0 }; //Register address 0-16
  
int ledstatus = 0;
int ledpin = 13;
AccelStepper stepper(AccelStepper::DRIVER, 3, 4);

/**
 *  Modbus object declaration
 *  u8id : node id = 0 for master, = 1..247 for slave
 *  port : serial port
 *  u8txenpin : 0 for RS-232 and USB-FTDI 
 *               or any pin number > 1 for RS-485
 */
Modbus slave(2,Serial,TXEN); // this is slave @1 and RS-485

void setup() {
  Serial.begin( 19200 ); // baud-rate at 19200
  pinMode(ledpin,OUTPUT);
  stepper.setMaxSpeed(3000);
  stepper.setAcceleration(1000);
  slave.start();
}

void loop() {
  slave.poll( au16data, 16 );
  if(au16data[2]== 1 ) {
    digitalWrite(ledpin,1);
    //stepper.setCurrentPosition(0);
    stepper.moveTo(6400*2); //Driver set 1/32 step --> .moveTo(6400) = move 1 rev
    // Run to target position with set speed and acceleration/deceleration:
    stepper.runToPosition();
    au16data[4]=stepper.currentPosition();
  }
  else if(au16data[2]== 0 ) {
    digitalWrite(ledpin,0);
    stepper.moveTo(0); //Driver set 1/32 step --> .moveTo(6400) = move 1 rev
    // Run to target position with set speed and acceleration/deceleration:
    stepper.runToPosition();
    au16data[4]=stepper.currentPosition();
  }
  
}
