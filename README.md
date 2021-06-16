# AquaBot
Aquaponics monitoring system

## Requirements

### Setting up your raspberry pi and monitoring station

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
- `pip install influxdb influx_line_protocol`
    - `sudo cp systemd/aquabot.service /lib/systemd/system/``
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

The temperature sensor script reads the output of the tempurature sensor on the GPIO pins, and writes the output to stdout.

It can be run using the following command.
```./temp-sensor.py
```

It will output logs to ./logs/temperature.log

## Telegraf-InfluxDB-Graphana Stack (TIG Stack


## Wiring Diagram

An equivalent diagram can be found here https://pimylifeup.com/raspberry-pi-temperature-sensor/.
