import boto3
import json

region = 'us-east-2'

ec2 = boto3.resource('ec2',region)

ImageId = 'ami-07efac79022b86107'
KeyName = 'aws_keypair'
InstanceType = 't2.micro'
#IamInstanceProfile =
instances = ec2.create_instances(
    ImageId =ImageId,
    MinCount = 1,
    MaxCount = 5,
    KeyName = KeyName,
    InstanceType = InstanceType,
    IamInstanceProfile = {
        'Name' : 'Test-ec2-pro',

    }
)
