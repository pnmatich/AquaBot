
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

## Notifications

Alerts and updates are delivered via email.

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

### Updates

Updates are sent via emails at scheduled or unschedules times

Scheduled updates:
- Weekly high, low, and average of all relevant sensors

Unscheduled updates:
- "nitrates high: you could have more plants!"
