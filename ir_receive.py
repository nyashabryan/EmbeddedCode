#!/usr/bin/python
# The receieving Pi embedded code

import RPi.GPIO as GPIO # import the RPIO.GPIO module

import time # Import the time module 

INPUT = 14
SIGNAL_FREQ = 3000
TRANSMISSION = False
BUFFER = []

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INPUT, GPIO.IN)

def receive():
    for i in range(16):
        BUFFER.append(GPIO.input(INPUT))
        time.sleep(1/(SIGNAL_FREQ))
    TRANSMISSION = False

def main():
    setup()
    try:
        while(1):
            GPIO.add_event_detect(INPUT, GPIO.RISING, callback=receive)
            TRANSMISSION = True
            while(TRANSMISSION):
                pass
            
    except KeyboardInterupt:
        GPIO.cleanup()
    GPIO.cleanup()

