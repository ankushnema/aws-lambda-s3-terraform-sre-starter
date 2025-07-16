# 📘 TECH_PRIMER.md – AWS Lambda + S3 + Terraform (SRE Starter)

This document is a technical walkthrough of the project structure and decisions. It explains how each component contributes to building a reliable, observable, and scalable serverless system — key to the Site Reliability Engineering (SRE) discipline.

---

## 🏗️ Infrastructure Breakdown (Terraform)

We use [Terraform](https://www.terraform.io/) to provision all AWS resources as code. This ensures reproducibility, version control, and faster iterations.

### 🔹 `provider` block
```hcl
provider "aws" {
  region = "us-east-1"
}
```
**Purpose:** Tells Terraform to work with AWS in the `us-east-1` region.

---

### 🔹 `aws_s3_bucket`
Creates an S3 bucket that serves as the event trigger source.

- **SRE Focus:** This decouples the event producer (S3) from the consumer (Lambda), making the system more modular and scalable.

---

### 🔹 `aws_lambda_function`
Defines the Lambda function, which:
- Is written in Python
- Pulls zipped code from the local `/lambda` folder
- Has an IAM role and environment variables set

```hcl
resource "aws_lambda_function" "s3_trigger_lambda" {
  ...
}
```

- **SRE Focus:** Serverless functions auto-scale and reduce operational overhead, aligning with SRE’s “reduce toil” principle.

---

### 🔹 `aws_iam_role` + `aws_iam_role_policy_attachment`
Grants minimal required permissions to Lambda using a secure, least-privilege model.

- **SRE Focus:** Secure by design, following the principle of least privilege.

---

### 🔹 `aws_lambda_permission` + `aws_s3_bucket_notification`
Links the S3 bucket to the Lambda so that any file upload automatically triggers event processing.

- **SRE Focus:** Clear event flow + declarative configuration = fewer surprises in production.

---

## 🐍 Lambda Function – Python

### 🔁 Retry Logic

We use the [`tenacity`](https://tenacity.readthedocs.io/en/latest/) library for exponential backoff retries:
- Retries up to 3 times
- Uses delays like 2s → 4s → 8s
- Logs each attempt and the final outcome

```python
@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=10))
```

- **SRE Focus:** Graceful failure handling improves system reliability without overloading downstream s
