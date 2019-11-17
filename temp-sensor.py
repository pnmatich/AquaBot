#!/usr/bin/python

import os
import glob
import logging
import time
from influxdb import InfluxDBClient

from influx_line_protocol import Metric

computerName=os.uname()[1]

if computerName != 'raspberrypi':
    raise Exception('Computer named {} is not named raspberrypi'.format(computerName))

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

logging.basicConfig(filename='logs/temperature.log', filemode='a', format='%(message)s', level=logging.INFO)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c = round(temp_c, 1) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL
        return temp_c

metric = Metric("AquaBot")

while True:
    temp_string='{0:0.1f}'.format(read_temp_c())
    now = int(round(time.time() * 1000000000))
    metric.with_timestamp(now)
    metric.add_tag('location', 'Surrey')
    metric.add_value('temperature', temp_string)
    print(metric)
    logging.info(metric)
