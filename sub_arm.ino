#if (ARDUINO >= 100)
  #include <Arduino.h>
#else
  #include <WProgram.h>
#endif

#include <ros.h>
#include <sensor_msgs/JointState.h>
#include <AccelStepper.h>
#include <MultiStepper.h>

AccelStepper joint1(AccelStepper::DRIVER, 2, 9);
AccelStepper joint2(AccelStepper::DRIVER, 3, 10);
AccelStepper joint3(AccelStepper::DRIVER, 4, 11);
AccelStepper joint4(AccelStepper::DRIVER, 5, 12);
AccelStepper joint5(AccelStepper::DRIVER, 6, 13);
AccelStepper joint6(AccelStepper::DRIVER, 7, 14);
AccelStepper joint7(AccelStepper::DRIVER, 8, 15);

int MaxSpeed_joint1 = 1000;
int MaxSpeed_joint2 = 1000;
int MaxSpeed_joint3 = 1000;
int MaxSpeed_joint4 = 1000;
int MaxSpeed_joint5 = 1000;
int MaxSpeed_joint6 = 1000;

MultiStepper steppers;

int joint_step[6];
int joint_status = 0;


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
ros::Subscriber<sensor_msgs::JointState> arm_sub("Ang",arm_cb);


void setup() {
 joint_status = 1;
 
 nh.initNode();
 nh.subscribe(arm_sub);
 
 Serial.begin(57600);
 
 joint1.setMaxSpeed(MaxSpeed_joint1);
 joint2.setMaxSpeed(MaxSpeed_joint2);
 joint3.setMaxSpeed(MaxSpeed_joint3);
 joint4.setMaxSpeed(MaxSpeed_joint4);
 joint5.setMaxSpeed(MaxSpeed_joint5);
 joint6.setMaxSpeed(MaxSpeed_joint6);
 
 steppers.addStepper(joint1);
 steppers.addStepper(joint2);
 steppers.addStepper(joint3);
 steppers.addStepper(joint4);
 steppers.addStepper(joint5);
 steppers.addStepper(joint6);
 
}

void loop() {
 if (joint_status == 1) // If command callback (arm_cb) is being called, execute stepper command
  { 
    Serial.print("joint_status == 1");
    
    long positions[6];  // Array of desired stepper positions must be long
    positions[0] = joint_step[0]; // negated since the real robot rotates in the opposite direction as ROS
    positions[1] = joint_step[1]; 
    positions[2] = -joint_step[2]; 
    positions[3] = joint_step[3]; 
    positions[4] = joint_step[4];
    positions[5] = joint_step[5];
    positions[6] = joint_step[6];
    
    Serial.print("  positions[1] = ");
    Serial.println(  positions[1]);
    
    steppers.moveTo(positions);
    nh.spinOnce();
    steppers.runSpeedToPosition(); // Blocks until all are in position
    
    Serial.println("::: pass move stepper :::");
  }
 joint_status = 0;
 Serial.println("joint_status = 0");
 nh.spinOnce();
 delay(1);
}
