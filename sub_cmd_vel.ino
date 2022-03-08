#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <robot_base/enc.h>

#include "CytronMotorDriver.h"

float duty_cycle=150;
float differential = 0.5;

// Pin variables for motors.
CytronMD motor1(PWM_DIR, 4, 5);   // PWM 1A = Pin 3, PWM 1B = Pin 9.
CytronMD motor2(PWM_DIR, 6, 7); // PWM 2A = Pin 10, PWM 2B = Pin 11.

// Pin Encoder 
#define ENC1A 2 // Yellow
#define ENC1B 3 // White
#define ENC2A 18 // Yellow
#define ENC2B 19 // White

int pos1 = 0;
int pos2 = 0;

robot_base::enc encoder;
ros::Publisher pub_enc("wheel_encoder", &encoder);

void cmd_vel_cb(const geometry_msgs::Twist & msg) {
  
  const float left_speed = msg.linear.x + msg.angular.z * differential ;
  const float right_speed = msg.linear.x - msg.angular.z * differential;
  //Serial.print(" msg.lineqar.x = ");
  //Serial.print(msg.linear.x);
  //Serial.print(" msg.angular.z = ");
  //Serial.print(msg.angular.z);
  //Serial.print(" Left = ");
  //Serial.print(left_speed);
  //Serial.print(" Right = ");
  //Serial.print(right_speed);
  
  int pwm1 = left_speed*1500;
  int pwm2 = right_speed*1500;
  
  motor1.setSpeed(pwm1);
  motor2.setSpeed(pwm2);
  
  //Serial.print(" pwm1 = ");
  //Serial.print(pwm1);
  //Serial.print(" pwm2 = ");
  Serial.println(pwm2);
  
}

ros::NodeHandle nh;
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", cmd_vel_cb);

void setup() {
  // ROS Setup
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  nh.advertise(pub_enc);
  nh.subscribe(sub);
  //Serial.begin(57600);
  
  pinMode(ENC1A,INPUT);
  pinMode(ENC1B,INPUT);
  pinMode(ENC2A,INPUT);
  pinMode(ENC2B,INPUT);
  attachInterrupt(digitalPinToInterrupt(ENC1A),readEncoder1,RISING );
  attachInterrupt(digitalPinToInterrupt(ENC2A),readEncoder2,RISING );
}

void loop() {
  //Serial.print("pos = ");
  //Serial.println(pos);
  
  pub_enc.publish( &encoder);
  nh.spinOnce();
  delay(1);
}

void readEncoder1(){
  int b = digitalRead(ENC1B);
  if(b > 0){
    pos1++;
  }
  else{
    pos1--;
  }
  encoder.enc_right = pos1;
}

void readEncoder2(){
  int b = digitalRead(ENC2B);
  if(b > 0){
    pos2++;
  }
  else{
    pos2--;
  }
  encoder.enc_left = pos2;
}
