resource "aws_iam_policy" "tfer--aquabot-002D-dynamo-002D-read-002D-policy" {
  name = "aquabot-dynamo-read-policy"
  path = "/"

  policy = <<POLICY
{
  "Statement": [
    {
      "Action": [
        "dynamodb:DescribeTable",
        "dynamodb:Scan",
        "dynamodb:Query"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:dynamodb:us-east-2:600496911827:table/AquaBotData",
      "Sid": "VisualEditor0"
    }
  ],
  "Version": "2012-10-17"
}
POLICY
}

resource "aws_iam_policy" "tfer--aws-002D-iot-002D-role-002D-dynamoPut_-002D-2102147375" {
  name = "aws-iot-role-dynamoPut_-2102147375"
  path = "/service-role/"

  policy = <<POLICY
{
  "Statement": {
    "Action": "dynamodb:PutItem",
    "Effect": "Allow",
    "Resource": "arn:aws:dynamodb:us-east-2:600496911827:table/AquaBotData"
  },
  "Version": "2012-10-17"
}
POLICY
}
