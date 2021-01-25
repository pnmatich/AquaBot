#!/bin/bash

# go to the directory this script is being run from
cd $(dirname $0)

echo directory name: $(dirname $0) >> ~/gitops.log

git pull origin master
