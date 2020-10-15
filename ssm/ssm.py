import boto3
import json
import time

region = 'us-east-2'

#ssm initialization
ssm = boto3.client('ssm',region)

#ec2 initialization
ec2 = boto3.resource('ec2',region)

#fetching instances only in running state
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


#running command on the targetted instnaces
response = ssm.send_command(
        InstanceIds = [j.id for j in instances],
        DocumentName = "AWS-RunShellScript",
        Parameters = {'commands': ['hostname']},
    )

#fetching command ids
command_id = response['Command']['CommandId']

#including a sleep time so that StatusDetails does not show InProgress
time.sleep(5)

#fetching commandid output for individual instances
for i in instances:
    output = ssm.get_command_invocation(
    CommandId = command_id,
    InstanceId = i.id,
    )
    print(output['StatusDetails'], output['StandardOutputContent'], i.id)
