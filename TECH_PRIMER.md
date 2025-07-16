# 📘 TECH_PRIMER.md – AWS Lambda + S3 + Terraform (SRE Starter)

This document is a technical walkthrough of the project structure and decisions. It explains how each component contributes to building a reliable, observable, and scalable serverless system — key to the Site Reliability Engineering (SRE) discipline.

---

## 🗂️ Terraform File Structure Explained

### **main.tf**
- **Purpose:**  The main configuration file where you define your cloud resources.
- **What goes here:**  All your AWS infrastructure (e.g., S3 bucket, Lambda, IAM roles).
- **Analogy:**  Think of `main.tf` as your project’s *blueprint*—it’s where you say what to build and how things are connected.
- **Is it mandatory?**  *The file name itself isn’t mandatory*, but you must have at least one `.tf` file with your infrastructure code. By convention, most projects use `main.tf` as the primary file for clarity.

### **variables.tf**
- **Purpose:**  To **define input parameters** that you want to configure dynamically (e.g., bucket name, region, environment).
- **What goes here:**  Variable definitions with type, description, and (optional) default values.
- **Analogy:**  Imagine you’re making a template; `variables.tf` is where you list the *fields people can customize*.
- **Is it mandatory?**  Not required by Terraform, but highly recommended for flexibility and reuse. If you hard-code everything in `main.tf`, you don’t need it—but it’s best practice to use variables.

### **outputs.tf**
- **Purpose:**  To **define what information Terraform should show you after applying**, such as resource names, ARNs, or URLs.
- **What goes here:**  Output blocks that reference your created resources (e.g., show the S3 bucket name or Lambda function name).
- **Analogy:**  Think of it as your *receipt or summary*—what you need to know or use after Terraform finishes.
- **Is it mandatory?**  No, but very helpful! Without outputs, you’d have to dig through AWS Console or Terraform state files to find resource names/IDs.

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

- **SRE Focus:** Graceful failure handling improves system reliability without overloading downstream systems.

---

### 🧾 Logging & Observability

We log:
- Incoming events
- Retry attempts
- Final success/failure status

Logs are sent to AWS CloudWatch and can be used to set alerts or track trends over time.

- **SRE Focus:** Observability is central to measuring reliability (SLIs, SLOs) and responding to incidents.

---

## 📈 Outputs

Terraform prints key outputs:
- S3 bucket name
- Lambda function name

These make testing and debugging easier.

---

## 🧠 Summary: Why This Matters for SRE

This small project touches on many core SRE principles:

| Principle                  | Implementation                                        |
|----------------------------|--------------------------------------------------------|
| **Infrastructure as Code** | Terraform manages all AWS resources                   |
| **Observability**          | Logs and retry events visible in CloudWatch           |
| **Graceful Degradation**   | Lambda retries failed executions with backoff         |
| **Security**               | IAM permissions scoped to minimum required            |
| **Scalability**            | Serverless architecture scales automatically          |
| **Reduced Toil**           | Automated setup and event handling                    |

---

## ✅ What’s Next

To extend this:
- Add metrics to CloudWatch (e.g., error rates)
- Trigger alerts based on failed retry attempts
- Convert the Lambda into a Docker container for more flexibility
- Deploy this using a CI/CD pipeline
