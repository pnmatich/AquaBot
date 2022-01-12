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
- set up passwordless ssh with ssh keys
    - https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md
    - create an ssh key on the monitoring station
        - `ssh-keygen -f ./AquaBot/rsync/ssh/id_rsa`
    - copy the public key to ~/.ssh/authorized_keys on the raspberrypi
- run some commands
    - `pip install influxdb influx_line_protocol`
    - `sudo cp pi/systemd/aquabot.service /lib/systemd/system/``
    - `sudo systemctl daemon-reload`
    - `sudo systemctl enable aquabot.service`
    - `sudo su`
    - `apt-get update`
    - `apt-get unstall pip`
    - `pip install influx influx_line_protocol`
    - `reboot`
- install gitops
    - Add a new ssh key in github for the new aquabot
    - `( crontab -l >> ~/.aquabot-gitops.log\n' ) | crontab`
    - `( crontab -l && printf -- 'echo * * * * *  /home/pi/Workshop/AquaBot/cron-gitops.sh >> ~/.aquabot-gitops.log\n' ) | crontab`

### Setting up your monitoring station (example uses arch linux package manager)

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

The temperature sensor script reads the output of the temperature sensor on the GPIO pins, and writes the output to stdout.

It can be run using the following command.
```./temp-sensor.py
```

It will output logs to ./logs/temperature.log

## Importer-InfluxDB-Graphana Stack (IIG Stack)

This project originally used a TIG Stack (Telegraf-InfluxDB-Graphana Stack), but the Telegraf component did not come to fruition. Instead an importer written in python is used to copy data from DynamoDB to the local InfluxDB database.

The importer copies up to 5000 datapoints every 5 seconds. This use close to 87.0 amazon read credits. AWS Free Tier allows for 25 amazon read credits every second. After a bit of math, the importer falls within the Free Tier range.



## Wiring Diagram

An equivalent diagram can be found here https://pimylifeup.com/raspberry-pi-temperature-sensor/.
