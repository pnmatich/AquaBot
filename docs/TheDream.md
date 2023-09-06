
# The Dream Implementation

This document aims to explain an ideal version of what AquaBot aims to be.

## Sensors

The AquaBot uses several sensors to determine the state of it's aquaponics system.

Sensors:
- high float (grow bed)
- low float (grow bed)
- low float (pond)
- thermometers
    - water
    - air
- luminosity
- pH
- oxygen
- ammonium
- nitrites NO2
- nitrates NO3

## Actuators

The AquaBot can effect the state of it's aquaponics system using several actuators

Actuators:
- pump kill switch
- pH up despenser
- pH down despenser
- fish feeder
- water fill switch

## Monitoring

The monitoring system can be deployed by running docker-compose up from the root directory of this project.

The grafana dashboard can be accessed at http://localhost:8080.

## Alerts and Notifications

Alerts and Notifications are delivered via email.

### Alerts

Alerts are sent as emails when the system is in an undesired state. Alerts sometimes include immediate follow up actions and additional alerts.

Alerts:
- "pump non-operational: harmful conditions for plants and fish"
- "ph high: harmful conditions for plants (and fish), actuating pH down"
    - if "pH high" or "pH low" has not been acted on in the last 12 hours, then
        - actuate pH down despenser
- "pH low: harmful conditions for fish (and plants), actuating pH up"
    - if "pH high" or "pH low" has not been acted on in the last 12 hours, then
        - actuate pH up despenser
- "pH raising too quickly: harmful conditions for fish"
- "pH falling too quickly: harmful conditions for fish"
- "grow bed stuck at high water: harmful conditions for plants, restarting"
    - restart pump (retry up to 5 times with 5 minute delay, then wait 12 hours)
- "grow bed stuck at low water: harmful conditions for plants"
    - restart pump (retry up to 5 times with 5 minute delay, then wait 12 hours)
- "pond at low water: potentially harmful conditions for fish"
    - if within 24 hours of last alert
        - "pond at low water again within 24 hours: pond leak"
    - actuate water fill switch for set time
        - if still at low water
            - kill pump and actuate water fill switch for set time
            - "pond still at low water after fill: potentially harmful conditions for fish (grow bed leak or pond leak)"
            - if still at low water
              - "pond still at water after additional fill: harmful conditions for fish (pond leak)
- "ammonium high: harmful conditions for fish"
- "nitrites high: harmful conditions for fish"

### Notifications

Notifications are sent via emails at scheduled or unschedules times

Scheduled notifications:
- Weekly high, low, and average of all relevant sensors

Unscheduled notifications:
- "nitrates high: you could have more plants!"

### AquaBot Registration

## AquaBot Initial setup

See [Automated Startup](docs/AutomatedStartup.md).

### Monitoring Station

The monitoring station can be set up on any computer that has docker and docker-compose installed. The grafana dashboard, influxdb local cache of dynamo db, and importer applications all run inside of docker containers. The can be built and stood up useing the following command.

```
docker-compose up -d && docker-compose logs -f importer
```

#### Create an AWS Role with required IAM access policies

#### Setting up registration credentials

to set up registration credentials on the registration machine. Create files called `credentials` and `config` in the `AquaBot/registration/credentials/aws/` folder on the machine being used to register AquaBots.

Example contents for `credentials`:
```
[default]
aws_access_key_id = <REDACTED>
aws_secret_access_key = <REDACTED>
```

Example contents for `config`:
```
[default]
region = us-east-2
```

#### Registering a new AquaBot with terraform

### AquaBot Raspberry Pi

This section is outdated! See See [Automated Startup](docs/AutomatedStartup.md).

Copy the certificate.pem, rootCA.pem, and private.key files from registration, to the AquaBot/credentials/ folder on the Raspberry Pi.

The Raspberry Pi AquaBot also needs to:
- have sensors attached to the correct pins
- add gitops cron job to the AquaBot crontab
  - the cron job runs the init script if `~/.aquabot/GitopsInit` is missing
    - the init script:
      - turns on One-Wire Interface
      - configures gpio pins
      - run script to register itself to AWS IoT and generate credentials files
      - adds service
      - creates and enables the AquaBot service
        - this service runs `pi/read-sensors.py`, every 5 seconds
  - the cron job pulls updates, and then runs a `cron/main.sh` script
    - this means updates to `main.sh` are pulled down before it is executed
    - if a tag matching the aquabot id does not exist
      - one is created saying the update was successful
      - this new tag is pushed back to github, so it can be viewed by the monitoring station

## Updates

Updates to the AquaBot repo are pulled down from gitlab via a cron job that runs every 5 minutes (see cron-gitops.sh).
