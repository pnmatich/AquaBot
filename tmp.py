#!/usr/bin/python

import os
import glob
import logging
import time
from influxdb import InfluxDBClient
from influx_line_protocol import Metric

import time


def read_temp_c():
        return '11.1'

def read_float_high():
    return False

def read_float_low():
    return True

metric = Metric("AquaBot")

while True:
    now = int(round(time.time() * 1000000000))
    metric.with_timestamp(now)
    metric.add_tag('location', 'Surrey')
    metric.add_value('temperature', read_temp_c())
    metric.add_value('float_high', read_float_high())
    metric.add_value('float_low', read_float_low())
    print(metric)
    logging.info(metric)
