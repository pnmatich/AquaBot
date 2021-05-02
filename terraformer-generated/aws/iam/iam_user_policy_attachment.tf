resource "aws_iam_user_policy_attachment" "tfer--ProgrammaticAccessUser_AdministratorAccess" {
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
  user       = "ProgrammaticAccessUser"
}

resource "aws_iam_user_policy_attachment" "tfer--dynamo-002D-db-002D-dummy-002D-iot-002D-access_aquabot-002D-dynamo-002D-read-002D-policy" {
  policy_arn = "arn:aws:iam::600496911827:policy/aquabot-dynamo-read-policy"
  user       = "dynamo-db-dummy-iot-access"
}
