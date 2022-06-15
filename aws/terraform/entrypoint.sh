#!/bin/bash

tf_state_bucket="aquabot-terraform-state-unique-identifier"

aws s3 mb s3://${tf_state_bucket} --region us-west-1
