# DEPLOY\_AND\_TEST.md — Deploy & Test AWS Lambda + S3 + Terraform Project (Mac)

This guide walks you through deploying, testing, and cleaning up your AWS Lambda + S3 + Terraform project on AWS.

---

## 🚀 Deployment & Testing Guide

### 1. Package Your Lambda Function

Make sure your Lambda code and dependencies (like `tenacity`) are included in the zip file:

```bash
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda

pip install --target . tenacity

zip -r lambda_function_payload.zip . -x "venv/*"
```

> If you already have your ZIP from earlier, you can skip this step.

---

### 2. Initialize and Apply Terraform

Change to your Terraform directory:

```bash
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/terraform
```

Run the following commands:

```bash
terraform init

terraform plan

terraform apply
```

> Type `yes` when prompted by `terraform apply`.

Watch the output to confirm resources are created (S3 bucket, Lambda function, IAM roles, etc).

---

### 3. Test Your Lambda and S3 Trigger

* Get your S3 bucket name from the Terraform output.
* Go to the AWS Console → S3 and find the new bucket.
* Upload any test file (e.g., a `.txt` file) to that S3 bucket.
* Go to AWS Console → CloudWatch → Logs → Log Groups and find your Lambda function’s logs.
* Check for log entries that show your Lambda was triggered and handled the event.

---

### 4. Review & Troubleshoot

* If you see logs showing the event was received and processed, your deployment is working!
* If you see errors, review logs and adjust code or configuration as needed.

---

### 5. Clean Up Resources When Done

To avoid AWS charges, destroy your stack:

```bash
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/terraform

terraform destroy
```

> Type `yes` when prompted.

---

## 🎉 Congratulations!

You’ve deployed, tested, and cleaned up your AWS Lambda + S3 project using Terraform.
