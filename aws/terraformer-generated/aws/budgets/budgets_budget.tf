resource "aws_budgets_budget" "tfer--Don-0027-t-0020-Spend-0020-Money" {
  account_id  = "600496911827"
  budget_type = "COST"

  cost_types {
    include_credit             = "true"
    include_discount           = "true"
    include_other_subscription = "true"
    include_recurring          = "true"
    include_refund             = "true"
    include_subscription       = "true"
    include_support            = "true"
    include_tax                = "true"
    include_upfront            = "true"
    use_amortized              = "false"
    use_blended                = "false"
  }

  limit_amount = "1.0"
  limit_unit   = "USD"
  name         = "Don't Spend Money"

  notification {
    comparison_operator        = "GREATER_THAN"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["pnmatich@gmail.com"]
    threshold                  = "50"
    threshold_type             = "PERCENTAGE"
  }

  time_period_end   = "2087-06-15_00:00"
  time_period_start = "2017-12-01_00:00"
  time_unit         = "MONTHLY"
}
