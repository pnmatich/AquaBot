#!/bin/bash

# NOTE: This script should be kept as simple as possible, because
# it is excecuted before changes to the git repo are pulled down.
# cron/main.sh is excecuted after changes are pulled down, so any
# commands to add should be added there.

set -x

# go to the directory this script is being run from
aquabotDirectory="$(dirname $0)"
cd ${aquabotDirectory}

echo "[INFO] - $(date) directory name: $(dirname $0)" >> ~/.aquabot-gitops.log
git fetch origin
git pull origin master --rebase

${aquabotDirectory}/cron/main.sh
