#!/usr/bin/python
 # The sending Pi embedded code
 import RPi.GPIO as GPIO # import the RPIO.GPIO module
 import time # Import the time module 
 CARRIER_OUT = 2
SIGNAL_OUT = 3
 CARRIER_FREQ = 38000
SIGNAL_FREQ = 3000
ON = True
OFF = False
 bit_stream = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0 ,1 , 1]
 def setup():
    global PWM_OUT, PWM_IN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CARRIER_OUT,GPIO.OUT)
    GPIO.setup(SIGNAL_OUT,GPIO.OUT)
    PWM_OUT = GPIO.PWM(CARRIER_OUT,CARRIER_FREQ)
    PWM_OUT.start(50)
 def onGPIO(bit):
    if bit == 1:
        return GPIO.HIGH
    return GPIO.LOW
 def sendbits():
    for bit in bit_stream:
        GPIO.output(SIGNAL_OUT, onGPIO(bit))
        time.sleep(1/(SIGNAL_FREQ))
    return OFF
 def main():
    setup()
    STATE = ON
    try:
        while(1):
            time.sleep(3)
            if (STATE):
                STATE = sendbits()
            GPIO.output(SIGNAL_OUT, GPIO.HIGH)
    except KeyboardInterupt:
        GPIO.cleanup()
    PWM.stop()
    GPIO.cleanup()
