
# Automated Startup and Updates

This document explains how the aquabot is initially setup, how it handles power faults, and how it is remotely updated.

## Initialization

Copy the certificate.pem, rootCA.pem, and private.key files from registration, to the AquaBot/credentials/ folder on the Raspberry Pi.

Run `./pi/configure-system.sh`, to add and enable `./pi/systemd/aquabot.service`.

## Remote Updates

The aquabot system uses a pull based method of updating itself. This method prevents the need to expose an endpoint for triggering updates. Instead, the aquabot system periodically polls its git repository, to check for updates.

## Fault Tolerance

If there is a temporary power outage, the system will be rebooted, and systemd will restart the service.