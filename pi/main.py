#!/usr/bin/python
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
log_msg="date and time:"+date_time
logging.info(log_msg)


import os
import subprocess

def run_command(cmd, cwd):
    """Helper function for running bash processes."""
    return subprocess.run(['/bin/bash', '-c', cmd], cwd=cwd, check=False)

homeDir="/home/pi"
workDir="/home/pi/Workshop"
abDir="/home/pi/Workshop/AquaBot"

run_command('date > .aquabot/test ', homeDir)
run_command('curl https://frightanic.com/goodies_content/docker-names.php > .aquabot/test ', homeDir)