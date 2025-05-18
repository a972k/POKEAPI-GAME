import boto3
import time
from botocore.exceptions import ClientError

#configure ec2 instance    
AMI_ID = "ami-04999cd8f2624f834"  
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "pokemon"  
SECURITY_GROUP_NAME = "pokemon-game-sg"
REPO_URL = "https://github.com/a972k/POKEAPI-GAME.git"
GAME_SCRIPT = "main.py"
REGION = "us-west-2"

#create boto3 EC2 client and resource
ec2_client = boto3.client("ec2", region_name=REGION)
ec2_resource = boto3.resource("ec2", region_name=REGION)

#get default vcp id
vpcs = ec2_client.describe_vpcs()
default_vpc_id = vpcs['Vpcs'][0]['VpcId']

#create or reuse security group
try:
    security_group = ec2_client.create_security_group(
        GroupName=SECURITY_GROUP_NAME,
        Description="Allow SSH access for Pokemon Game",
        VpcId=default_vpc_id
    )
    ec2_client.authorize_security_group_ingress(
        GroupId=security_group["GroupId"],
        IpPermissions=[{
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }]
    )
    print(f"created security group: {SECURITY_GROUP_NAME}")
except ClientError as e:
    if "InvalidGroup.Duplicate" in str(e):
        print(f"security group '{SECURITY_GROUP_NAME}' already exists.")
        sg = ec2_client.describe_security_groups(GroupNames=[SECURITY_GROUP_NAME])
        security_group = {"GroupId": sg["SecurityGroups"][0]["GroupId"]}
    else:
        raise

#user data script to set up the app deplioyment
user_data_script = f'''#!/bin/bash
yum update -y
yum install -y git python3
cd /home/ec2-user
git clone {REPO_URL}
echo "cd /home/ec2-user/POKEAPI-GAME" >> /home/ec2-user/.bashrc
echo "python3 {GAME_SCRIPT}" >> /home/ec2-user/.bashrc
'''

#launch ec2 instance
print("[*] launching ec2 instance...")
instance = ec2_resource.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[security_group["GroupId"]],
    UserData=user_data_script
)[0]

#wait until it's running
print("waiting for instance to be in 'running' state...")
instance.wait_until_running()
instance.reload()

#confirm running status and print details
status = instance.state['Name']
if status == 'running':
    print("ec2 instance is running and ready!")
    print(f"public DNS: {instance.public_dns_name}")
    print(f"connect with: ssh -i your-key.pem ec2-user@{instance.public_dns_name}")
    print("pokemon game will start automatically on login.")
else:
    print("Instance is not running. Current state:", status)

#cleanup function for later use
# def cleanup_instance(instance_id):
#     print(f"terminating instance {instance_id}...")
#     ec2_client.terminate_instances(InstanceIds=[instance_id])
#     print("terminated.")
