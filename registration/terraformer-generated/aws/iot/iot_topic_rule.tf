resource "aws_iot_topic_rule" "tfer--handball_aquabot_data_to_dynamodb" {
  dynamodb {
    hash_key_field  = "id"
    hash_key_type   = "STRING"
    hash_key_value  = "${topic()}"
    payload_field   = "payload"
    range_key_field = "timestamp"
    range_key_type  = "NUMBER"
    range_key_value = "${timestamp()}"
    role_arn        = "arn:aws:iam::600496911827:role/service-role/aquabot-dynamo-update-role"
    table_name      = "AquaBotData"
  }

  enabled     = "true"
  name        = "handball_aquabot_data_to_dynamodb"
  sql         = "SELECT * FROM 'aquabot-data'"
  sql_version = "2016-03-23"
}
