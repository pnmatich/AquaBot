#!/usr/bin/python3

import os
import glob
import logging
import RPi.GPIO as GPIO
from time import sleep, time
from subprocess import PIPE, run
from influxdb import InfluxDBClient
from influx_line_protocol import Metric

computerName=os.uname()[1]

if computerName != 'raspberrypi':
    raise Exception('Computer named {} is not named raspberrypi'.format(computerName))

# Setup float sensor pins
GPIO.setmode(GPIO.BCM)
# GPIO 23 & 17 set up as inputs.
GPIO.setup(23, GPIO.IN)
GPIO.setup(17, GPIO.IN)

# Setup temp sensor pins
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

logging.basicConfig(filename='/home/pi/Workshop/AquaBot/logs/temperature.log', filemode='a', format='%(message)s', level=logging.INFO)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c = round(temp_c, 1) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL
        return temp_c

def read_float_high():
    if str(GPIO.input(17)) == "1":
        return 3
    else:
        return 0

def read_float_low():
    if str(GPIO.input(23)) == "1":
        return 1
    else:
        return 0

dateCommand = ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"]

starttime=time()
while True:
    date = run(dateCommand, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    run(["mosquitto_pub",
    "--cert",   "./credentials/certificate.pem",
    "--cafile", "./credentials/rootCA.pem",
    "--key",    "./credentials/private.key",
    "-d",
    "-h",       "alvftq0926je9-ats.iot.us-east-2.amazonaws.com",
    "-p",       "8883",
    "-q",       "1",
    "-t",       "aquabot-data",
    "-m",
    r'{"measurement": "sensor_readings",' +
    r'"time": "' + date.stdout.rstrip() + r'",' +
    r'"fields": {' +
    r'"temperature": ' + str(read_temp_c()) + r',' +
    r'"float_low": '   + str(read_float_low()) + r',' +
    r'"float_high": '  + str(read_float_high()) + r'}}'])
    sleep(5 - ((time() - starttime) % 5))
