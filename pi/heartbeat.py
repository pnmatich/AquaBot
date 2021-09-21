#!/usr/bin/python3

import os
import glob
import logging
from time import sleep, time
from subprocess import PIPE, run
from influxdb import InfluxDBClient
from influx_line_protocol import Metric

computerName=os.uname()[1]

if computerName != 'raspberrypi':
    raise Exception('Computer named {} is not named raspberrypi'.format(computerName))

logging.basicConfig(filename='/home/pi/Workshop/AquaBot/logs/temperature.log', filemode='a', format='%(message)s', level=logging.INFO)

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
    r'"heartbeat": "true"}}'])
    sleep(5 - ((time() - starttime) % 5))
