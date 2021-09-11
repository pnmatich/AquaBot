#!/bin/bash

mkdir -p ~/Workshop
cd ~/Workshop
rm -rf ./AquaBot
git clone git@github.com:pnmatich/AquaBot.git
cd ./AquaBot
git config --global user.email "pnmatich@gmail.com"
git config --global user.name "Paul Matich AquaBot Bravo"
