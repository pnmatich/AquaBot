resource "aws_iot_thing" "tfer--AquaBot1" {
  attributes = {
    ph          = "unknown"
    temperature = "unknown"
  }

  name            = "AquaBot1"
  thing_type_name = "AquaBot"
}

resource "aws_iot_thing" "tfer--Aquabot-002D-20180903" {
  attributes = {
    draining = "0"
  }

  name            = "Aquabot-20180903"
  thing_type_name = "Aquabot"
}
