provider "aws" {
  region = "ap-northeast-2" # Please use the default region ID
}

# S3 bucket for backend
# link: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_versioning
resource "aws_s3_bucket" "tfstate" {
  bucket = "${var.account_id}-apne2-tfstate-backend"
}

# resource "aws_s3_bucket_acl" "example" {
#   bucket = aws_s3_bucket.example.id
#   acl    = "private"
# }

resource "aws_s3_bucket_versioning" "tfstate" {
  bucket = aws_s3_bucket.tfstate.bucket

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_dynamodb_table" "terraform_state_lock" {
  name           = "terraform-lock"
  hash_key       = "LockID"
  billing_mode   = "PAY_PER_REQUEST"

  attribute {
    name = "LockID"
    type = "S"
  }
}

variable "account_id" {
  default = "kafka-from-scratch"
}