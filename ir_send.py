#!usr/bin/python
# Sending PI Embedded Code

import RPi.GPIO as GPIO

import time

CARRIER_OUT = 
SIGNAL_OUT = 

CARRIER_FREQ = 38000
SIGNAL_FREQ = 3000
ON = True
OFF = False

bit_stream = [1,1,0,0,0,1,1,1,0, 1]

def setup():
	global PWM_OUT
	GPIO.setmode()
