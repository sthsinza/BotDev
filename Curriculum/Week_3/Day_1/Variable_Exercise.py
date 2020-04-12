
import RPi.GPIO as GPIO
from time import sleep

"""
First we need to initialize variables that will tell
the python interpreter which GPIO (General Purpose Input/Output)
pins talk to our stepper motor drivers...
in other words when we want to send our motor drivers a message,
which pin should we use to send it?
We need three pin for each motor driver:
1) enable pin: when this pin is off (yeah off) the motor is enabled
2) direction pin: when this pin is on the motor will rotate in one direction
    and when it is off it will rotate in the other
3) Step pin: when we turn this pin on, we tell the motor to take a step
    to the next position... we will turn it on and off very quickly
    to make the motors rotate
"""
rightEnable = 17
rightDir = 22
rightStep = 27

leftEnable = 5
leftDir = 26
leftStep = 6

"""We don't need no stinking warnings we live dangerously!!!!"""
GPIO.setwarnings(False)

"""There are more than one pin map for the Raspberry pi.
The two most common pin maps are BCM and Wiring Pi...
We will use BCM (Broadcom SOC Channel numbers) for this program"""
GPIO.setmode(GPIO.BCM)

"""Now we need to set up the GPIO pins.  GPIO pins are normally
set to either input or output pins.  This means that you
either use the pins to talk to components -like motor- or
components like sensors use the pins to talk to the program
for this program we only need to talk to the motors"""
GPIO.setup(rightStep, GPIO.OUT)
GPIO.setup(leftStep, GPIO.OUT)
GPIO.setup(rightDir, GPIO.OUT)
GPIO.setup(leftDir, GPIO.OUT)
GPIO.setup(rightEnable, GPIO.OUT)
GPIO.setup(leftEnable,GPIO.OUT)

"""So now lets calculate how many step we need to
take to move forward one inch!
Our wheels have a diameter of 110mm (4.33 in.).
So the circumference of the wheel is C = 2pi * r
C = (2*3.14159) * 55mm = 6.28318 * 55mm = 345.6mm
or 13.6 inches.
The rotational angle of one step (step angle) is
1.8 degrees.  So a 1/4 step is 0.45 degrees. This
means our motor will complete one revolution in 800
 1/4 steps.  360/0.45 = 800.
Since the diameter of our wheel is 13.6 in: then
one inch worth of rotation is defined by 800/13.6.
Therefore 58.8 steps equals one inch... we'll
have to round up. 
"""
inchSteps = 59 

"""As we learned above we need to tell the motor
to take steps really fast to get it to rotate.
So to tell the motor to switch from one phase to
the next advancing the motor 1.8 degrees need to
turn it on and off.  We will need a slight delay
between turning it on and off to allow the motor
time to rotate... a few milliseconds should do it!"""

delay = .0025

"""Let's make a couple variable for defining the
direction that a motor should rotate.  When we turn
a pin "on" we say we set the pin to 'HIGH' and when
we turn it off we say we set the pin to 'LOW.' HIGH
means we are sending 5 volts through the pin, LOW
means we are sending 0 volts through the pin.  We
can represent the HIGH state as GPIO.HIGH or True
or 1.  We can represnt LOW as GPIO.LOW, or False or
0."""

fwd = 1
bwd = 0

"""Now let's define a function to move the STEMBot
forward or backward for a number of inches provided
as a parameter."""

def move(direction, inches):
    """first lets enable the motors and
        set their direction"""
    GPIO.output(rightEnable, GPIO.LOW)
    GPIO.output(leftEnable, GPIO.LOW)
    GPIO.output(rightDir, direction)
    GPIO.output(leftDir, direction)
    
    """Now lets calculate how many steps we need
    to take inorder to travel the number of inches
    the 'inches' parameter instructs us to go...
    remember we calculated how many step are in
    an inch above and stored it in a variable call
    inchSteps"""
    numOfSteps = inches * inchSteps;
    
    """Now that we know how many steps to take lets
    use a loop to repeat the process of turning the
    assocviated GPIO pins on and off until we've taken
    all the steps we need."""
    
    for x in range(numOfSteps):
        GPIO.output(rightStep, GPIO.HIGH)
        GPIO.output(leftStep, GPIO.HIGH)
        sleep(delay)
        GPIO.output(rightStep, GPIO.LOW)
        GPIO.output(leftStep, GPIO.LOW)
        sleep(delay)
    
    sleep(1)
    """Finally, let's disable the motors so they don't
    have to hold the current from the battery"""
    GPIO.output(rightEnable, GPIO.HIGH)
    GPIO.output(leftEnable, GPIO.HIGH)

"""Now lets see if we can write some code to turn the
STEMBot to a specific angle.  The STEMBot's wheelbase
-the distance from the center of one wheel to the other-
is 140mm, the means if it turn an entire 360 degrees
both wheels would travel a diameter of 439.8mm.  C= 2Pi * r
C = (2*3.14159) * 70mm = 6.28318 * 70mm = 439.8mm
Therefore 439.8/360 is the number of millimeters each wheel
must travel to turn one degree: 1.2mm.  We know from above that
the wheel has a circumference of 345.6mm/800 1/4steps = 0.432mm So
we first calculate the distance the wheels must travel to
make the turn then divide that number by 0.432 to get the number
of steps each motor must take"""

def turn(direction, degrees):
    #distance = degrees * 1.2
    #steps = distance/1.5
    distance = degrees * 1.2
    steps = distance/0.4
    
    GPIO.output(rightEnable, GPIO.LOW)
    GPIO.output(leftEnable, GPIO.LOW)
    if direction:  
        GPIO.output(rightDir, 1)
        GPIO.output(leftDir, 0)
    else:
        GPIO.output(rightDir, 0)
        GPIO.output(leftDir, 1)
        
    for x in range(int(steps)):
        GPIO.output(rightStep, GPIO.HIGH)
        GPIO.output(leftStep, GPIO.HIGH)
        sleep(delay)
        GPIO.output(rightStep, GPIO.LOW)
        GPIO.output(leftStep, GPIO.LOW)
        sleep(delay)
    
    """Finally, let's disable the motors so they don't
    have to hold the current from the battery"""
    sleep(1)
    GPIO.output(rightEnable, GPIO.HIGH)
    GPIO.output(leftEnable, GPIO.HIGH)

"""Flip a coin out in front of the STEMBot and follow the
Steps below to define a path to move the STEMBot to the
coin"""

"""First determine how far you wish to travel in the first leg 
of your path.  Assign the leg_1 variable to the distance you
wish to travel in inches
"""
leg_1 = 2

"""Now determine whether you need to turn left or right.
Assign the turn_direction variable to True to turn right
and False to turn left.
"""

turn_direction = True

"""Determine how far the STEMBot should rotate in 
degrees and assign the turn_degrees variable to the 
degrees you wish to turn
"""

turn_degrees = 90

"""Finally determine the length of the last leg of
your path to stop on top of the coin"""

leg_2 = 2

"""Now run the program"""

try:
    if __name__ == "__main__":
        
        move(True,leg_1)
        turn(turn_direction,turn_degrees)
        move(True,leg_2)
        

except KeyboardInterrupt:
    GPIO.cleanup()

