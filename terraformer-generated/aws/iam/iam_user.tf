resource "aws_iam_user" "tfer--AIDAJL7GYFJSQZINCXVE6" {
  force_destroy = "false"
  name          = "dynamo-db-dummy-iot-access"
  path          = "/"
}

resource "aws_iam_user" "tfer--AIDAJNSKOF3BNMN2Y5S2C" {
  force_destroy = "false"
  name          = "ProgrammaticAccessUser"
  path          = "/"
}
