#!/bin/bash

piAddress="192.168.0.109"
piLogDirectory="/home/pi/Workshop/AquaBot/logs"

while inotifywait -r -e ssh pi@${piAddress}:${piLogDirectory} modify,create,delete,move /directory; do
    rsync -avz ./logs ${piLogDirectory}
done
