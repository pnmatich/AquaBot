#!/bin/sh

piAddress="192.168.0.109"
piLogDirectory="/home/pi/Workshop/AquaBot/logs"

while true; do
    echo "[INFO] - syncing logs from raspberrypi"
    rsync -r -e "ssh -o StrictHostKeyChecking=no" --info=progress2 pi@${piAddress}:${piLogDirectory} /AquaBot/
    sleep 10
done
