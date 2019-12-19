#!/usr/bin/env python2.7
# original script by Alex Eames https://raspi.tv
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs. One pulled up, the other down.
# 23 will go to GND when button pressed and 17 will go to 3V3 (3.3V)
# this enables us to demonstrate both rising and falling edge detection
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# now we'll define the threaded callback function
# this will run in another thread when our event is detected

def edge_callback(channel):
    print('raising or falling edge detected on channel %s'%channel)

print "Make sure you have a button connected so that when pressed"
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
print "You will also need a second button connected so that when pressed"
print "it will connect GPIO port 17 (pin ?) to 3V3 (pin 1)"
raw_input("Press Enter when ready\n>")

# The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on port 17, regardless of whatever
# else is happening in the program, the function "my_callback" will be run
# It will happen even while the program is waiting for
# a falling edge on the other button.
GPIO.add_event_detect(23, GPIO.BOTH, callback=edge_callback)
GPIO.add_event_detect(17, GPIO.BOTH, callback=edge_callback)

while True:
    time.sleep(1)

#    except KeyboardInterrupt:
#        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
#    GPIO.cleanup()           # clean up GPIO on normal exit
