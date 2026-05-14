import boto3
# Create EC2 resource
ec2 = boto3.resource('ec2', region_name='ap-south-1')
# ✅ User Data Script (auto runs on launch)
user_data_script = """#!/bin/bash
yum update -y
yum install -y httpd

systemctl start httpd
systemctl enable httpd

echo "<h1>🚀 Hello Namit! Server deployed using boto3</h1>" > /var/www/html/index.html
"""

# Launch instance
instances = ec2.create_instances(
    ImageId='ami-0e12ffc2dd465f6e4',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='automation-key',
    UserData=user_data_script   # ✅ added this
)

instance = instances[0]

print("🚀 Launching EC2 with auto deployment...")

# Wait until running
instance.wait_until_running()
instance.load()

print(f"✅ Instance ID: {instance.id}")
print(f"🌐 Public IP: {instance.public_ip_address}")