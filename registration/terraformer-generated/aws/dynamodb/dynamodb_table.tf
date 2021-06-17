resource "aws_dynamodb_table" "tfer--AquaBotData" {
  attribute {
    name = "timestamp"
    type = "N"
  }

  attribute {
    name = "id"
    type = "S"
  }

  billing_mode = "PROVISIONED"
  hash_key     = "id"
  name         = "AquaBotData"

  point_in_time_recovery {
    enabled = "false"
  }

  range_key      = "timestamp"
  read_capacity  = "5"
  stream_enabled = "false"
  write_capacity = "5"
}
