"""These are the two libraries that we will use for this program"""
import RPi.GPIO as GPIO
import time
from time import sleep
""" The library need to know which pin numbering system you are going to use.
    There are more than one pin map for the Raspberry PI. 
    We will use BCM (Broadcom SOC Channel numbers) for this program"""

GPIO.setmode(GPIO.BCM)

"""The HC-SR04 ultrasonic sensor has 4 pins. VCC, Gnd, Trig and echoLeft.
   VCC connects to the 5V in the raspberry pi.Gnd connects to one of the ground pins. Trig
   activates the sensors which needs to be connected to one of the GPIO
   output pin. echoLeft returns the signal which must be read from the GPIO input pin."""


rightEnable = 17
rightDir = 22
rightStep = 27

leftEnable = 5
leftDir = 26
leftStep = 6
triggerLeft = 16
echoLeft =  12
triggerCenter = 18 
echoCenter = 24
triggerRight = 23
echoRight = 25

GPIO.setwarnings(False)

GPIO.setup(rightStep, GPIO.OUT)
GPIO.setup(leftStep, GPIO.OUT)
GPIO.setup(rightDir, GPIO.OUT)
GPIO.setup(leftDir, GPIO.OUT)
GPIO.setup(rightEnable, GPIO.OUT)
GPIO.setup(leftEnable,GPIO.OUT)
GPIO.setup(triggerLeft, GPIO.OUT)
GPIO.setup(echoLeft, GPIO.IN)
GPIO.setup(triggerCenter, GPIO.OUT)
GPIO.setup(echoCenter, GPIO.IN)
GPIO.setup(triggerRight, GPIO.OUT)
GPIO.setup(echoRight, GPIO.IN)

inchSteps = 59 
delay = .0025
fwd = 1
bwd = 0

def smartStop(trig, echo, loc):
    
    """The triggerLeft pin needs to be set low"""
    GPIO.output(trig, True)
    
    """Ultrasonic has a reccommended cycle period of 50ms,
        which is the amount of time you should wait to take measurement.
        But we will go ahead and make it wait for 100ms.
        sleep() takes in seconds in the parameter.
        1 second = 1000ms
        1 ms = 1/1000 = 0.001
        0.01ms = 0.001 * 100ms = 0.01ms
    """
    #We need a short delay for the sensors to settle.
    time.sleep(0.01)
    # We then need to set the triggerLeft to high after 0.01ms
    GPIO.output(trig, False)
    
    """The time() method returns the number of seconds passed
        since epoch. For Unix system, Jan 1, 1970, 00:00:00 at UTC is epoch.
        In other words, tt expresses the current time in seconds."""
    
    startTime = time.time()
    stopTime = time.time()
    
    while GPIO.input(echo) == 0:
        startTime = time.time()
    
 
    while GPIO.input(echo) == 1:
        stopTime = time.time()
    
    timeElasped = stopTime - startTime
        
    distance = round((6800 * timeElasped),2)
    
    print("Obstacle near ", loc, "sensor: ")
    print(distance, "in")
    isobstacle = False
    if (distance < 10):
        print(distance, "in")
        isobstacle = True
    
            
    return isobstacle
    
def move(direction, inches):
   
    GPIO.output(rightEnable, GPIO.LOW)
    GPIO.output(leftEnable, GPIO.LOW)
    GPIO.output(rightDir, direction)
    GPIO.output(leftDir, direction)
    
 
    numOfSteps = inches * inchSteps;
    
    
    for x in range(numOfSteps):
        GPIO.output(rightStep, GPIO.HIGH)
        GPIO.output(leftStep, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(rightStep, GPIO.LOW)
        GPIO.output(leftStep, GPIO.LOW)
        #time.sleep(delay)
        if(x%200==0):
            if(smartStop(triggerLeft, echoLeft, "Left") or smartStop(triggerRight, echoRight, "Right") or smartStop(triggerCenter, echoCenter, "Center")):
                print("loop broken")
                break
        else:
            time.sleep(delay)
    time.sleep(1)
   
    GPIO.output(rightEnable, GPIO.HIGH)
    GPIO.output(leftEnable, GPIO.HIGH)

def turn(direction, degrees):
   
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
        
        if(x%45==0):
            if(smartStop(triggerLeft, echoLeft, "Left") or smartStop(triggerRight, echoRight, "Right") or smartStop(triggerCenter, echoCenter, "Center")):
                print("loop broken")
                break
        #time.sleep(1)
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


try:
    if __name__ == "__main__":
        
        
        move(True,12)
        turn(True, 90)
     
    

except KeyboardInterrupt:
    GPIO.cleanup()

    