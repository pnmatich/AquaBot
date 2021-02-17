#!/bin/bash

set -x

# go to the directory this script is being run from
cd $(dirname $0)

echo "[INFO] - $(date) directory name: $(dirname $0)" >> ~/.aquabot-gitops.log

git pull origin master --rebase

if [[ ! $(git describe --exact-match $(git rev-parse HEAD) 2>/dev/null) =~ ^ab.*$ ]]; then
  tag_name="ab-$(date +"%Y-%m-%dT%H-%M-%S%Z")"
  git tag -a "${tag_name}" -m "🌞 $(date +"%Y-%m-%dT%H:%M:%S%Z") - Successful aquabot deployment"
  git push origin ${tag_name}
fi
