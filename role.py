import boto3
import json


#session = boto3.session.Session(profile_name='my_profile')

iam = boto3.client('iam') #iam client initialization
ec2 = boto3.resource('ec2','us-east-2') #ec2 resource initialization
path = '/'
role_name = 'ec2-test-role'
description = 'BOTO3 ec2 test role'

trust_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

role = iam.create_role(
    Path = path,
    RoleName = role_name,
    AssumeRolePolicyDocument = json.dumps(trust_policy),
    Description = "allows SSM full access to ec2 instances",
    MaxSessionDuration = 3600
)

response = iam.attach_role_policy(
    RoleName = role_name,
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonSSMFullAccess'
)

instance_profile = iam.create_instance_profile(
    InstanceProfileName = 'Test-ec2-pro',
    Path = '/'
)

iam.add_role_to_instance_profile(InstanceProfileName='Test-ec2-pro',
    RoleName=role_name
)

ImageId = 'ami-07efac79022b86107'
KeyName = 'aws_keypair'
InstanceType = 't2.micro'
#IamInstanceProfile =
instances = ec2.create_instances(
    ImageId =ImageId,
    MinCount = 1,
    MaxCount = 1,
    KeyName = KeyName,
    InstanceType = InstanceType,
    IamInstanceProfile = {
        'Name' : 'Test-ec2-pro',

    }
)
