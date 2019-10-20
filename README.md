# AquaBot
Aquaponics monitoring system

## Setting up the raspberry pi

The raspberry pi for this project should be setup to use the raspbian operating system.

The following additional steps should also be taken:
- run `sudo raspi-config`, and turn on the One-Wire Interface
- append `dtoverlay=w1-gpio,gpiopin=4` to /boot/config.txt
- run `sudo modprobe w1–gpio`
- reboot the system (you might need to run this step between each of the above steps)

## Temperature sensor python script

The temperature sensor script reads the output of the tempurature sensor on the GPIO pins, and writes the output to stdout.

It can be run using the following command.
```./temp-sensor.py

