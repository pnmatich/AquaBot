#!/bin/bash

# Create id file if it does not already exist
id_file='~/aquabot/id'

echo "[INFO] - $(date) running cron main.sh" >> ~/.aquabot-gitops.log


if [ ! -f ${id_file} ]; then
  mkdir -p ~/aquabot
  echo "ab-1" > ${id_file}
fi

# Create and push git tag if one does not already exist
if [[ ! $(git describe --exact-match $(git rev-parse HEAD) 2>/dev/null) =~ ^ab.*$ ]]; then
  tag_name="ab-$(date +"%Y-%m-%dT%H-%M-%S%Z")"
  git tag -a "${tag_name}" -m "🌞 $(date +"%Y-%m-%dT%H:%M:%S%Z") - Successful remote deployment to aquabot"
  git push origin ${tag_name}
  sudo service aquabot restart
  touch ~/.aquabot-log
fi
