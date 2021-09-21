#!/bin/bash

# Create id file if it does not already exist
if [ ! -f ~/aquabot/id ]; then
  echo "[INFO] - $(date) creating id file" >> ~/.aquabot-gitops.log
  mkdir -p ~/aquabot
  echo "ab2" > ~/aquabot/id
fi

aquabot_id=$(cat ~/aquabot/id)

# Create and push git tag if one does not already exist
if [[ ! $(git describe --exact-match $(git rev-parse HEAD) 2>/dev/null) =~ ^ab.*$ ]]; then
  echo "[INFO] - $(date) tagging commit" >> ~/.aquabot-gitops.log

  tag_name="${aquabot_id}-$(date +"%Y-%m-%dT%H-%M-%S%Z")"
  echo "[INFO] - creating and pushing tag ${tag_name}" >> ~/.aquabot-gitops.log
  git tag -a "${tag_name}" -m "🌞 - Successful remote deployment to aquabot"
  git push origin ${tag_name}
  sudo service aquabot restart
fi
