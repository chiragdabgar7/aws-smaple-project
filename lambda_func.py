import boto3
import json

#client = boto3.client('lambda')

def lambda_build(LambdaFunctionName, iamRole):
    client = boto3.client('lambda')

    create_lambda_function = client.create_function(
        FunctionName=LambdaFunctionName,
        Runtime='python3.7',
        Role=iamRole,
        Handler='{}.lambda_build'.format('lambda_func'),
        Description='Start a virtual machine',
	    Code = {'S3Bucket':'test-bucket-chirag20201510', 'S3Key':'ssm.zip'}
        )
    return create_lambda_function


print(lambda_build('My_func2','arn:aws:iam::<your-account-number>:role/lambda-test-role'))
