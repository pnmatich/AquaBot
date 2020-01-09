#!/usr/bin/python
# original script by Alex Eames https://raspi.tv
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs.
GPIO.setup(23, GPIO.IN)
GPIO.setup(17, GPIO.IN)

raw_input("Press Enter when ready\n>")

while True:
    time.sleep(1)

    print "High Float: " + str(GPIO.input(17))
    print "Low Float:" + str(GPIO.input(23))
