#!/bin/bash

set -x

if [[ ! $(git describe --exact-match $(git rev-parse HEAD) 2>/dev/null) =~ ^ab.*$ ]]; then
  tag_name="ab-$(date +"%Y-%m-%dT%H-%M-%S%Z")"
  git tag -a "${tag_name}" -m "🌞 $(date +"%Y-%m-%dT%H:%M:%S%Z") - Successful remote deployment to aquabot"
  git push origin ${tag_name}
  sudo service aquabot restart
fi
