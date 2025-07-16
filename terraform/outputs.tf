
output "lambda_function_name" {
  value = aws_lambda_function.s3_trigger_lambda.function_name
}

output "s3_bucket_name" {
  value = aws_s3_bucket.lambda_trigger_bucket.bucket
}
