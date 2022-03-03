#if (ARDUINO >= 100)
  #include <Arduino.h>
#else
  #include <WProgram.h>
#endif
#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <AccelStepper.h>
#include <MultiStepper.h>

AccelStepper joint1(1,8,15);
int joint_step[6] = {0,0,0,0,0,0};
int joint_status = 0;

MultiStepper steppers;

void arm_cb(const sensor_msgs::JointState& arm_steps){
  joint_status = 1;
  joint_step[0] = arm_steps.position[0];
  joint_step[1] = arm_steps.position[1];
  joint_step[2] = arm_steps.position[2];
  joint_step[3] = arm_steps.position[3];
  joint_step[4] = arm_steps.position[4];
  joint_step[5] = arm_steps.position[5];
  Serial.print("joint1 = ");
  Serial.println( joint_step[1]);
}
ros::NodeHandle nh;
ros::Subscriber<sensor_msgs::JointState> arm_sub("ArmJointState",arm_cb);


void setup() {
 nh.initNode();
 nh.subscribe(arm_sub);
 Serial.begin(57600);
 joint1.setMaxSpeed(1000);
 steppers.addStepper(joint1);
 
}

void loop() {
 if (joint_status == 1) // If command callback (arm_cb) is being called, execute stepper command
  { 
    Serial.print("joint111 = ");
    Serial.println( joint_step[1]);
    long positions[6];  // Array of desired stepper positions must be long
    positions[1] = joint_step[1]; // negated since the real robot rotates in the opposite direction as ROS
    Serial.print("  positions[1] = ");
    Serial.println(  positions[1]);
    steppers.moveTo(positions);
    nh.spinOnce();
    steppers.runSpeedToPosition(); // Blocks until all are in position
    Serial.println("BBBBBBBBB");
  }
 Serial.println("AAAAAAAALLLL");
 //prev_pos[1] = positions[1]
 joint_status = 0;
 nh.spinOnce();
 delay(1);
}
