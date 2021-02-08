#!/bin/bash

set -x

# go to the directory this script is being run from
cd $(dirname $0)

echo $(date) directory name: $(dirname $0) >> ~/.aquabot-gitops.log

git pull origin master --rebase

if [[ ! $(git describe --exact-match $(git rev-parse HEAD) 2>/dev/null) =~ ^ab.*$ ]]; then
  tag_name="ab-$(date +%s)"
  git tag -a "${tag_name}" -m "🌞 $(date +"%Y-%m-%dT%H:%M:%S%Z") - Successful deployment to aquabot"
  git push origin ${tag_name}
fi
