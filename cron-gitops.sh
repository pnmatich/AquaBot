#!/bin/bash

# go to the directory this script is being run from
cd $(dirname $0)

echo cd $(dirname $0) >> ~/.gitops.log

git pull origin master
