#!/usr/bin/python
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
log_msg="date and time:"+date_time
logging.info(log_msg)