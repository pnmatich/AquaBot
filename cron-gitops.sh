#!/bin/bash

set -x

# go to the directory this script is being run from
aquabotDirectory="$(dirname $0)"
cd ${aquabotDirectory}

echo "[INFO] - $(date) directory name: $(dirname $0)" >> ~/.aquabot-gitops.log
git fetch origin
git pull origin master --rebase

${aquabotDirectory}/cron/main.sh
