content = """
# 🏃‍♂️ RUN_GUIDE.md — Complete Step-by-Step Setup & Run Guide for AWS Lambda + S3 + Terraform Project (Mac)

This guide will help you run your Lambda + S3 + Terraform SRE Starter Project end-to-end on your Mac, using AWS Free Tier. It includes prerequisites, setup, deployment, testing, cleanup, and troubleshooting—all in one place.

---

## 🤔 Before You Begin: What Are Homebrew, HashiCorp, and Tap?

- **`brew`** is the command-line tool for **Homebrew**, the most popular package manager for Mac. It lets you easily install, update, and manage software like Python, Git, Terraform, etc.
- **HashiCorp** is the company behind Terraform and other DevOps tools.
- **`tap`** in Homebrew means “add a new software source/repository.”  
  `brew tap hashicorp/tap` adds HashiCorp’s official tools (like Terraform) to your Homebrew install list.

---

## ✅ Step 1: Install Prerequisites

1. **Install Terraform**
    ```bash
    brew tap hashicorp/tap
    brew install hashicorp/tap/terraform
    terraform -version
    ```

2. **Install AWS CLI**

   **What is AWS CLI?**  
   - AWS CLI stands for **Amazon Web Services Command Line Interface**.
   - It lets you control your AWS account from the Terminal, automating tasks like creating S3 buckets, deploying Lambda functions, and more—no browser needed!
   - Required by Terraform to authenticate and deploy resources to your AWS account.
  
    ```bash
    brew install awscli
    aws --version
    ```

3. **Configure AWS CLI**
    ```bash
    aws configure
    ```
    - Enter your AWS access key, secret, default region (`us-east-1`), and output format (`json`).
    - If you don’t have AWS keys, generate them here: https://console.aws.amazon.com/iam/home#/security_credentials
    - Default region name [None]: us-east-1
    - Default output format [None]: json 

4. **Confirm Python 3.9+ and pip are available**

   ### 🤖 What is pip?
   - **`pip` is Python’s package installer.**
   - Lets you easily add new features to your Python code by installing extra libraries (like `tenacity` for retry logic).
   - Used to bundle required libraries with your AWS Lambda code so everything runs smoothly in the cloud.

    ```bash
    python3 --version
    pip3 --version
    ```

5. **(Optional for local editing) Install Lambda dependency**

   ### 🛡️ Installing Python Dependencies Safely (Virtual Environment)

**Recent Macs protect the system Python.  
Best practice:** Use a virtual environment for any project dependencies.

**To install the `tenacity` library (or others) in your lambda folder:**

1. **Create a virtual environment:**
    ```bash
    cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    _(You’ll see `(venv)` at the start of your terminal line.)_

3. **Install tenacity (and other dependencies) inside the virtual environment:**
    ```bash
    pip install tenacity
    ```

4. **Deactivate when done (optional):**
    ```bash
    deactivate
    ```

**Tip:**  
Always activate the virtual environment before installing or running Python code with extra dependencies!

---

## ✅ Step 2: Package the Lambda Code

From your lambda directory:
```bash
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda
zip -r lambda_function_payload.zip lambda_function.py
