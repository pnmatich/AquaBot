#!/bin/bash

# NOTE: This script should be kept as simple as possible, because
# it is excecuted before changes to the git repo are pulled down.
# cron/main.sh is excecuted after changes are pulled down, so any
# commands to add should be added there.

# go to the directory this script is being run from
aquabotDirectory="$(dirname $0)"
cd ${aquabotDirectory}

git fetch;
LOCAL=$(git rev-parse HEAD);
REMOTE=$(git rev-parse @{u});

#if our local revision id doesn't match the remote, we will need to pull the changes
if [ $LOCAL != $REMOTE ]; then
    #pull and merge changes
    git pull origin master;
fi

echo "[INFO] - $(date) running cron main.sh" >> ~/.aquabot-gitops.log
${aquabotDirectory}/cron/main.sh &>> ~/.aquabot.log
