import boto3

ec2 = boto3.client('ec2') # Construct EC2 client
response = ec2.describe_instances()
print(response)

  