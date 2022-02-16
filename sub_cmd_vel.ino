#if (ARDUINO >= 100)
#include <Arduino.h>
#else
#include <WProgram.h>
#endif
#include <ros.h>
#include <geometry_msgs/Twist.h>
#include "CytronMotorDriver.h"

int duty_cycle=100;
int differential = 0.5;

// Pin variables for motors.
CytronMD motor1(PWM_PWM, 3, 9);   // PWM 1A = Pin 3, PWM 1B = Pin 9.
CytronMD motor2(PWM_PWM, 10, 11); // PWM 2A = Pin 10, PWM 2B = Pin 11.

void SetMotorMode(String motor, String direct,int pwm){
    if(motor == 'leftmotor'){
        if(direct == 'backward'){
              motor1.setSpeed(pwm);
        }
        else if (direct == 'forward'){
              motor1.setSpeed(-pwm);
        }
    }
    if (motor == 'rightmotor'){
        if (direct == 'backward'){
            motor2.setSpeed(pwm);
        }
        else if(direct == 'forward'){
            motor2.setSpeed(-pwm);
        }
    }

}

void SetMotorLeft( const float vel){
  if (vel < 0){
      int pwm = -(duty_cycle * vel);
      if (pwm > duty_cycle){
          pwm = duty_cycle;
      }
      // PWMA.ChangeDutyCycle(pwm)
      SetMotorMode("leftmotor", "backward",pwm);
      
  }
  else if (vel > 0){
      int pwm = duty_cycle * vel;
      if (pwm > duty_cycle){
          pwm = duty_cycle;
      }
     
      SetMotorMode("leftmotor", "forward",pwm);
  }
}

void SetMotorRight( const float vel){
  if (vel < 0){
      int pwm = -(duty_cycle * vel);
      if (pwm > duty_cycle){
          pwm = duty_cycle;
      }
      SetMotorMode("rightmotor", "backward",pwm);
      
  }
  else if (vel > 0){
      int pwm = duty_cycle * vel;
      if (pwm > duty_cycle){
          pwm = duty_cycle;
      }
      SetMotorMode("rightmotor", "forward",pwm);
  }
}

void cmd_vel_cb(const geometry_msgs::Twist & msg) {
  const float left_speed = msg.linear.x - msg.angular.z * differential ;
  const float right_speed = msg.linear.x + msg.angular.z * differential;
  SetMotorLeft(left_speed);
  SetMotorRight(right_speed);  
}

ros::NodeHandle nh;
ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", cmd_vel_cb);

void setup() {
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}
