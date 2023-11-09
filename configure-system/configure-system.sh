#!/bin/bash

mkdir -p ~/aquabot
mkdir -p ~/Workshop
cd ~/Workshop
git clone git@github.com:pnmatich/AquaBot.git
cd ./AquaBot
git config pull.rebase true
git config --global user.email "pnmatich@gmail.com"
git config --global user.name "Paul Matich AquaBot"

sudo cp pi/systemd/aquabot.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable aquabot.service

# These files need to be copied to the pi
# "./credentials/certificate.pem"
# "./credentials/rootCA.pem"
# "./credentials/private.key"
