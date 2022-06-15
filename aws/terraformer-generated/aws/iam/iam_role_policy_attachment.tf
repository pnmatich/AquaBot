resource "aws_iam_role_policy_attachment" "tfer--AWSServiceRoleForSupport_AWSSupportServiceRolePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/aws-service-role/AWSSupportServiceRolePolicy"
  role       = "AWSServiceRoleForSupport"
}

resource "aws_iam_role_policy_attachment" "tfer--AWSServiceRoleForTrustedAdvisor_AWSTrustedAdvisorServiceRolePolicy" {
  policy_arn = "arn:aws:iam::aws:policy/aws-service-role/AWSTrustedAdvisorServiceRolePolicy"
  role       = "AWSServiceRoleForTrustedAdvisor"
}

resource "aws_iam_role_policy_attachment" "tfer--aquabot-002D-dynamo-002D-update-002D-role_aws-002D-iot-002D-role-002D-dynamoPut_-002D-2102147375" {
  policy_arn = "arn:aws:iam::600496911827:policy/service-role/aws-iot-role-dynamoPut_-2102147375"
  role       = "aquabot-dynamo-update-role"
}
