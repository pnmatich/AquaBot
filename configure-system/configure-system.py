#!/usr/bin/python3

'''
This is a multiline
comment.

This script:
- sets up systemd test scripts
- sets up required directories
- clones required directories
- copies required keys and certs
- does this all idempotently
'''

import os
import subprocess

def run_command(cmd, cwd):
    """Helper function for running bash processes."""
    return subprocess.run(['/bin/bash', '-c', cmd], cwd=cwd, check=False)

homeDir="/home/pi"
workDir="/home/pi/Workshop"
abDir="/home/pi/Workshop/AquaBot"

if not os.path.isdir("/home/pi/Workshop/AquaBot"):
    run_command('git clone git@github.com:pnmatich/AquaBot.git', workDir)


# Create necessary directories if they don't already exist
run_command('mkdir -p aquabot', homeDir)
run_command('mkdir -p Workshop', homeDir)

run_command('git config pull.rebase true', abDir)
run_command('git config --global user.email "pnmatich@gmail.com"', abDir)
run_command('git config --global user.name "Paul Matich AquaBot"', abDir)
run_command('git fetch origin', abDir)
run_command('git pull origin main', abDir)

run_command('git fetch origin', abDir)
run_command('git pull origin main', abDir)
run_command('sudo cp pi/systemd/aquabot.service /lib/systemd/system/', abDir)
run_command('sudo systemctl daemon-reload', abDir)
run_command('sudo systemctl enable aquabot.service', abDir)

# These files need to be copied to the pi
# "./credentials/certificate.pem"
# "./credentials/rootCA.pem"
# "./credentials/private.key"
