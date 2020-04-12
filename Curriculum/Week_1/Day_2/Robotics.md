![Image description](https://github.com/BotDevLLC/BotDevCurriculum/blob/master/Pictures/Botdev.png)
# VITAL INFORMATION
Subject(s): Robotics  

 

Topic or Unit: Introduction to STEMBot 

 

Grade/Level: 8th Grade 

 

Time Allotment: 30 minutes 

 

Standards:           3.4.5. A3. Describe how technologies are often combined.  

  3.4.6. A3. Explain how knowledge from other fields of study (STEM) integrate to create new technologies.   

  3.4.6. D2. Use computers appropriately to access and organize and apply information 

 

Unit Goal(s):      By the end of the unit, students will have a basic understanding of how STEMBot works.  

 

Objective(s):      Students should measure the path and write function calls to make the STEMBot travel the through the maze ending in the destination box 
# INSTRUCTIONAL PROCEDURES 
  # What is STEMBot? 
  STEMBot is a robot designed for learning. STEMBot is an open source project with full curriculum and educational resources. Nothing about the STEMBot is simple, but it is all easy to learn. Let’s get started! 


1. Use masking tape to create a simple maze on the floor with a starting box and a destination box. Ensure to make several 90 degree turns. 

2. Point out the parts of the STEMBot to students.  It has a Raspberry Pi (RPi) for a microcontroller/microcomputer.  The RPi is the brain of the STEMBot, it runs the programs and sends commands to the other components.  The STEMBot has two stepper motors that are controlled individually to make the STEMBot move.  These stepper motors rely on two motor drivers make them rotate.  The RPi has GPIO (General Purpose Input/Output) pins that it uses to talk to the motor drivers.  When we run a program the RPi will use these pins to sends commands to the motor drivers that will then send electrical current to motors to make them rotate. 

3. The motor drivers use integrated circuits to switch the electrical current to different coils in the motor to make it rotate.  This falls into the electrical engineering field, while the program to control the STEMBot can be considered to be part of the Software Engineering field.  The physical design of the STEMBot falls into the Mechanical Engineering field.  And lots of math is required.  A programmer must calculate the circumference of the wheels to determine how to make the STEMBot move forward a designated distance or turn a specified number of degrees.  (Review the code in the “FirstRun.py” program for more details).  Discuss these various STEM fields with students.  

4. Instructor will then open VNC into the raspberry pi and open the “FirstRun.py” program on the Desktop. Describe the functions programmed at the bottom (move, turn, etc). 

    a. See Week 1 Day 3 unit: “Communicating with STEMBot” for VNC guidance. 

    b. See Week 1 Day 4 unit: “Basic CLI Commands and Running Python Code from Terminal” for guidance in running Python programs.  

5. Provide the student with tape measures or yard sticks.  Students will measure the path and write function calls in python program to make the STEMBot travel the through the maze ending in the destination box. 

# MATERIALS AND RESOURCES
* STEMBot(s) 
* Computer(s) 
* Internet (Optional if the STEMBot has its own router) 
* Measuring Tape 
* Masking Tape 

 

