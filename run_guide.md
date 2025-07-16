# RUN\_GUIDE.md — Complete Step-by-Step Setup & Run Guide for AWS Lambda + S3 + Terraform Project (Mac)

This guide will help you run your Lambda + S3 + Terraform SRE Starter Project end-to-end on your Mac, using AWS Free Tier. It includes prerequisites, explanations, setup, deployment, testing, cleanup, troubleshooting, and best practices—all in one place.

---

## Before You Begin: What Are Homebrew, HashiCorp, Tap, AWS CLI, and pip?

* **`brew`** is the command-line tool for **Homebrew**, the most popular package manager for Mac. It lets you easily install, update, and manage software like Python, Git, Terraform, etc.
* **HashiCorp** is the company behind Terraform and other DevOps tools.
* **`tap`** in Homebrew means “add a new software source/repository.”
  `brew tap hashicorp/tap` adds HashiCorp’s official tools (like Terraform) to your Homebrew install list.
* **AWS CLI** stands for **Amazon Web Services Command Line Interface**. It lets you control your AWS account from Terminal, automating tasks like creating S3 buckets, deploying Lambda functions, and more—no browser needed! It’s also required by Terraform to authenticate and deploy resources to your AWS account.
* **`pip`** is Python’s package installer. It lets you easily add new features to your Python code by installing extra libraries (like `tenacity` for retry logic). It’s used to bundle required libraries with your AWS Lambda code so everything runs smoothly in the cloud.

---

## Step 1: Install Prerequisites

1. **Install Homebrew (if not already installed):**

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Terraform**

   ```bash
   brew tap hashicorp/tap
   brew install hashicorp/tap/terraform
   terraform -version
   ```

3. **Install AWS CLI**

   ```bash
   brew install awscli
   aws --version
   ```

---

## Step 2: Configure AWS CLI

**What is AWS CLI?**
AWS CLI lets you control AWS from your Terminal and is required for Terraform deployments.

**Configure AWS CLI:**

aws configure

Enter your AWS Access Key ID, Secret Access Key, default region (like us-east-1), and output format (json).

If you don’t have AWS keys, create them at: AWS Security Credentials

What is Default Region Name?

It’s the AWS “location” for your resources. Most users pick us-east-1 (N. Virginia).

What is Default Output Format?

Choose json for compatibility with scripts and Terraform.

## Step 3: Verify Python and pip

**What is pip?**
pip is Python’s package installer for adding extra features to your code.

**Check your versions:**

```
bash
```

CopyEdit

`python3 --version pip3 --version`

You should see Python 3.9+ and pip 21.x or higher.

---

## Step 4: Install Python Dependencies Safely (Virtual Environment Recommended)

Recent Macs protect system Python. **Best practice:** Use a virtual environment for dependencies.

To install the `tenacity` library in your lambda folder:

**Create a virtual environment:**

```
bash
```

CopyEdit

`cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda python3 -m venv venv`

**Activate the virtual environment:**

```
bash
```

CopyEdit

`source venv/bin/activate`

(You’ll see `(venv)` at the start of your terminal line.)

**Install tenacity (and other dependencies):**

```
bash
```

CopyEdit

`pip install tenacity`

**Deactivate when done (optional):**

```
bash
```

CopyEdit

`deactivate`

> **Tip:** Always activate the virtual environment before installing or running Python code with extra dependencies!

---

## Step 5: Package the Lambda Code

If using dependencies (like tenacity), install them directly into your lambda folder:

```
bash
```

CopyEdit

`cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda pip install --target . tenacity`

**Zip everything in the lambda directory (excluding the venv folder if desired):**

```
bash
```

CopyEdit

`zip -r lambda_function_payload.zip . -x "venv/*"`

The ZIP must be named as referenced in your Terraform code.

---

## Step 6: Deploy Infrastructure with Terraform

```
bash
```

CopyEdit

`cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/terraform terraform init terraform plan terraform apply`

Type `yes` when prompted.

---

## Step 7: Test Lambda and S3 Trigger

* Get your S3 bucket name from the Terraform output.
* Upload any file to the S3 bucket via the AWS Console.
* Open AWS CloudWatch → Logs → Log Groups → Find your Lambda function.
* Review logs to see retry attempts, event details, and success/failure.

---

## Step 8: Clean Up Resources When Done

```
bash
```

CopyEdit

`terraform destroy`

---

## Troubleshooting & FAQ

**Q: Lambda fails with \`ModuleNotFoundError: No module named 'tenacity'?**
You need to package external Python libraries with your Lambda code. For simple projects, install dependencies locally in your lambda folder, then zip everything (excluding venv):

```
bash
```

CopyEdit

`cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda pip install --target . tenacity zip -r lambda_function_payload.zip . -x "venv/*"`

Update your Terraform code to reference the correct zip file if needed.

---

**Q: I get AWS permission errors?**
Ensure your AWS IAM user has permissions for S3, Lambda, IAM, and CloudWatch. For personal/test accounts, attach `AdministratorAccess` (never use in production).

---

**Q: Region errors or missing logs?**
Make sure you’re using the same region everywhere (`us-east-1` by default).
