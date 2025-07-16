# AWS Lambda + S3 Trigger — Terraform SRE Starter

This project sets up a reliable, serverless event-driven architecture using AWS Lambda and S3, provisioned via Terraform. It demonstrates core Site Reliability Engineering (SRE) principles like observability, graceful failure handling, and infrastructure as code (IaC).

## 🌍 Use Case

When a new object is uploaded to an S3 bucket, a Lambda function is triggered to process the event. The function includes retry logic and structured logging, helping ensure that transient failures are automatically retried and logged for analysis.

---

## 🚀 What This Project Includes

- ✅ AWS Lambda function written in Python 3.9
- ✅ S3 bucket trigger on object upload
- ✅ Terraform-based infrastructure provisioning
- ✅ Retry logic with exponential backoff using `tenacity`
- ✅ Observability via structured logs (viewable in CloudWatch)
- ✅ Beginner-friendly project structure and documentation

---

## 🛠️ Getting Started

### Prerequisites

- AWS CLI configured (`aws configure`)
- Terraform installed
- Python 3.9+
- Git

### Setup Steps

1. Clone the repo  
   ```bash
   git clone https://github.com/ankushnema/aws-lambda-s3-terraform-sre-starter.git
   cd aws-lambda-s3-terraform-sre-starter
