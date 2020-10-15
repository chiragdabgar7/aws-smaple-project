import boto3
import json

iam = boto3.client('iam')

path = '/'
role_name = 'lambda-test-role'
description = 'BOTO3 lambda test role'

trust_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

#create lambda use case role
role = iam.create_role(
    Path = path,
    RoleName = role_name,
    AssumeRolePolicyDocument = json.dumps(trust_policy),
    Description = "allows SSM full access to lambda instances",
    MaxSessionDuration = 3600
)

#attach ssm full access to policy to the role
response1 = iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonSSMFullAccess'
)

#attach lambda full access policy to the role
response2 = iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = 'arn:aws:iam::aws:policy/AWSLambdaFullAccess'
)

#creating instance profile
instance_profile = iam.create_instance_profile(
    InstanceProfileName = 'Test-lambda-pro',
    Path = '/'
)

#add role to the above created instance profile
iam.add_role_to_instance_profile(InstanceProfileName='Test-lambda-pro',
    RoleName=role_name
)
