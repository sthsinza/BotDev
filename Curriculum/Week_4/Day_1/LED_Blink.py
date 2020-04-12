import RPi.GPIO as GPIO    #This imports Raspbery Pi GPIO Library
from time import sleep     #This imports the sleep function from the time module
"""Why do we need to import GPIO and sleep? We do this because we are going to initialize
    the GPIO ports on the Raspberry Pi. We want the Led light to blink so having a sleep
    timer when the Led light is on and off will make it blink."""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)



GPIO.output(4, GPIO.HIGH)   #This will turn the Led light on
sleep(0.5)
GPIO.output(4, GPIO.LOW)   #This will turn the led light off
sleep(0.5)
GPIO.output(4, GPIO.HIGH)
sleep(0.5)
GPIO.output(4, GPIO.LOW)
sleep(0.5)    
