resource "aws_iot_thing_type" "tfer--AquaBot" {
  deprecated = "true"
  name       = "AquaBot"

  properties {
    description           = "Aquaponics monitoring system"
    searchable_attributes = ["temperature", "ph"]
  }
}

resource "aws_iot_thing_type" "tfer--Aquabot" {
  deprecated = "false"
  name       = "Aquabot"

  properties {
    searchable_attributes = ["draining", "ph", "temperature"]
  }
}
