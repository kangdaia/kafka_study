### Create policies for allowing user to assume the role in the production account
### You can copy this file and change `prod` to other environment if you have any other account

# Admin Access policy 
# If this policy is applied, then you will be able to assume role in the production account with admin permission
module "production_admin" {
  source      = "./_module_assume_policy/"
  aws_account = "kafka-from-scratch-prod"
  subject     = "admin"
  resources   = ["arn:aws:iam::${var.prod_account_id}:role/assume-kafka-from-scratch-prod-admin"]
}

output "assume_production_admin_policy_arn" {
  value = module.production_admin.assume_policy_arn
}

# Poweruser Access policy 
# If this policy is applied, then you will be able to assume role in the production account with poweruser permission
module "production_poweruser" {
  source      = "./_module_assume_policy/"
  aws_account = "kafka-from-scratch-prod"
  subject     = "poweruser"
  resources   = ["arn:aws:iam::${var.prod_account_id}:role/assume-kafka-from-scratch-prod-poweruser"]
}

output "assume_production_poweruser_policy_arn" {
  value = module.production_poweruser.assume_policy_arn
}


# ReadOnly Access policy 
# If this policy is applied, then you will be able to assume role in the production account with readonly permission
module "production_readonly" {
  source      = "./_module_assume_policy/"
  aws_account = "kafka-from-scratch-prod"
  subject     = "readonly"
  resources   = ["arn:aws:iam::${var.prod_account_id}:role/assume-kafka-from-scratch-prod-readonly"]
}

output "assume_production_readonly_policy_arn" {
  value = module.production_readonly.assume_policy_arn
}