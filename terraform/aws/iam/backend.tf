terraform {
  backend "s3" {
    bucket         = "kafka-from-scratch-apne2-tfstate-backend" # Set bucket name 
    key            = "terraform/iam/kafka-from-scratch/terraform.tfstate"
    region         = "ap-northeast-2"
    encrypt        = true
    dynamodb_table = "terraform-lock" # Set DynamoDB Table
  }
}