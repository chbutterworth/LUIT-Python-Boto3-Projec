# Imports Boto3 module to local environment
import boto3
# Defining variable for script to work with a Boto3 method
ec2 = boto3.client('ec2')
# A specific variable for script to exclude "Cloud9" tag attatched to "Cloud9" instance running this SDE
cloud9 = {'Key':'Env', 'Value':'Cloud9'}
# Calling AWS to collect instance data and making it a variable to manipulate.
response = ec2.describe_instances()
# Manipulating AWS data just collected to hone in on area of interest for instances.
reservations = response['Reservations']
# For-Loop to pull information from an nested list of dictionaries within the AWS data.
for reservation in reservations:
    instances = reservation['Instances']
# For-Loop to pull nested information from list of dictionaries from 'Instances' list.
# For-Loop also iterates through entire list of 'Instances'
    for instance in instances:
# Logic to exclude "Cloud9" instance and include instances that are running
        if cloud9 not in instance['Tags'] and 'running' in instance['State']['Name']:
            print(instance['InstanceId'])
# For-loop and logic to pull "Name" value from tags in order to print it on a distinct line.
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    print(tag['Value'])
# Boto3 method to stop instances with input being the list filtered instance ids remaining.
            ec2.stop_instances(InstanceIds=[instance['InstanceId']])
            print('Instance Stopped')
            print()