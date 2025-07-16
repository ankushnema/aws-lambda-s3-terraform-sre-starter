
# AWS Lambda + S3 + Terraform Starter (SRE Focused)

This project provisions an AWS Lambda function triggered by an S3 upload event using Terraform. It includes retry logic using Python's `tenacity` library to simulate and handle transient failures.

## Features
- AWS Lambda function written in Python
- S3 bucket trigger on object upload
- Terraform-based infrastructure
- Retry logic with exponential backoff
- Logging for observability (viewable in CloudWatch)

## Setup Steps

1. Install prerequisites:
    - AWS CLI
    - Terraform
    - Python 3.9+
2. Run `terraform init`, `terraform plan`, `terraform apply`
3. Upload any file to the created S3 bucket
4. Check logs in AWS CloudWatch

## Retry Logic
The Lambda retries the operation up to 3 times with exponential backoff in case of random failures (simulated).

## Clean Up
To remove resources:
```
terraform destroy
```
