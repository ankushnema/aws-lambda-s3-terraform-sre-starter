✅ Step 1: Install Prerequisites
Install Terraform

bash
Copy
Edit
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
terraform -version
Install AWS CLI

bash
Copy
Edit
brew install awscli
aws --version
Configure AWS CLI

bash
Copy
Edit
aws configure
Enter your AWS access key, secret, default region (us-east-1), and output format (json).

If you don’t have AWS keys, generate them here: https://console.aws.amazon.com/iam/home#/security_credentials

Confirm Python 3.9+ and pip are available

bash
Copy
Edit
python3 --version
pip3 --version
(Optional for local editing) Install Lambda dependency

bash
Copy
Edit
pip3 install tenacity

✅ Step 2: Package the Lambda Code
From your lambda directory:

bash
Copy
Edit
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda
zip -r lambda_function_payload.zip lambda_function.py
The ZIP must be named as referenced in Terraform.

If your Lambda function imports external libraries (like tenacity) and you want to test on AWS:
Install the dependency in the lambda folder and zip everything:

bash
Copy
Edit
pip3 install --target . tenacity
zip -r lambda_function_payload.zip .

✅ Step 3: Deploy Infrastructure with Terraform
bash
Copy
Edit
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/terraform
terraform init
terraform plan
terraform apply
Type yes when prompted.

✅ Step 4: Test Lambda and S3 Trigger
Get your S3 bucket name from the Terraform output.

Upload any file to the S3 bucket via the AWS Console.

Open AWS CloudWatch → Logs → Log Groups → Find your Lambda function.

Review logs to see retry attempts, event details, and success/failure.

✅ Step 5: Clean Up Resources When Done
bash
Copy
Edit
terraform destroy

🧠 Troubleshooting & FAQ
Q: Lambda fails with ModuleNotFoundError: No module named 'tenacity'?
A: You need to package external Python libraries with your Lambda code. For simple projects, install dependencies locally in your lambda folder, then zip everything:

bash
Copy
Edit
cd ~/Downloads/aws-lambda-s3-terraform-sre-starter/lambda
pip3 install --target . tenacity
zip -r lambda_function_payload.zip .
Update your Terraform if needed to use the new zip.

Q: I get AWS permission errors?
A: Ensure your AWS IAM user has permissions for S3, Lambda, IAM, and CloudWatch. If needed, attach AdministratorAccess (for personal/test accounts only).

Q: Region errors or missing logs?
A: Make sure you’re using the same region everywhere (us-east-1 by default).

