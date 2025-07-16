
# TECH PRIMER: AWS Lambda + S3 + Terraform Explained

## Terraform Files

### `provider` block
Tells Terraform you're using AWS and which region.

### `aws_s3_bucket`
Creates an S3 bucket that will trigger the Lambda.

### `aws_lambda_function`
Defines the Lambda function:
- Uses Python runtime
- Takes zipped code
- Sets environment variables (like retry attempts)

### `aws_iam_role` and `policy_attachment`
IAM role for the Lambda function to run with minimal permissions.

### `aws_s3_bucket_notification`
Links the S3 bucket to the Lambda, so that file uploads trigger it.

## Python Code

- Uses `tenacity` to implement retry with exponential backoff.
- Randomly simulates failure to showcase retry.
- Logs events at each stage, viewable in CloudWatch.

## Observability

- Logs are automatically shipped to AWS CloudWatch.
- Retry failures and successes are clearly logged.

## Relevance to SRE Role

- IaC (Terraform) ensures reproducible environments
- Logging + retry demonstrates graceful failure handling
- Tight integration of cloud resources mirrors real SRE workflows
