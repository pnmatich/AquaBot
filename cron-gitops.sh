#!/bin/bash

# go to the directory this script is being run from
cd $(dirname $0)


echo $(date) directory name: $(dirname $0) >> ~/.aquabot-gitops.log

git pull origin master
