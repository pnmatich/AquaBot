# AquaBot
Aquaponics monitoring system

## Requirements

### Setting up your raspberry pi

The raspberry pi for this project should be setup to use the raspbian operating system.

The following additional steps should also be taken:
- run `sudo raspi-config`, and turn on the One-Wire Interface
- append `dtoverlay=w1-gpio,gpiopin=4` to /boot/config.txt
- run `sudo modprobe w1–gpio`
- reboot the system (you might need to run this step between each of the above steps)

### Setting up your arch linux box

#### Installing docker

```sudo pacman -S docker
sudo pacman -S docker-compose
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker
systemctl status docker.service
```

#### Installing python packages

`pip install influx_line_protocol`

## Temperature sensor python script

The temperature sensor script reads the output of the tempurature sensor on the GPIO pins, and writes the output to stdout.

It can be run using the following command.
```./temp-sensor.py
```

It will output logs to ./logs/temperature.log

## Telegraf-InfluxDB-Graphana Stack (TIG Stack)
