#!/bin/bash -x

id_file='/aquabot/id'

if [ ! -f ${id_file} ]; then
  mkdir -p /aquabot
  echo "ab-1" > ${id_file}
fi
