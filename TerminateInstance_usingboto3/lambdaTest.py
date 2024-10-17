import boto3
from datetime import datetime, timezone, timedelta

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Fetch all EC2 instances
    instances = ec2_client.describe_instances()
    
    # Get the current time
    current_time = datetime.now(timezone.utc)
    
    # Set the time limit (24 hours ago)
    time_limit = current_time - timedelta(days=1)
    
    # Set the time limit (1 minute ago)
    #time_limit = current_time - timedelta(minutes=1)
    
    
    terminated_instances = []
     
     # Loop through the instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            # Get the instance ID and launch time
            instance_id = instance['InstanceId']
            launch_time = instance['LaunchTime']  
            
            # Compare launch time with the time limit
            if launch_time < time_limit:
                # Terminate the instance
                ec2_client.terminate_instances(InstanceIds=[instance_id])
                # Add to the terminated instances list
                terminated_instances.append({
                    'InstanceId': instance_id,
                    'LaunchTime': str(launch_time)
                })
    
    # If instances were terminated, log them
    if terminated_instances:
        print("Terminated EC2 Instances:")
        for instance in terminated_instances:
            print(f"Instance ID: {instance['InstanceId']}, LaunchTime: {instance['LaunchTime']}")
    else:
        print("No EC2 instances older than 1 minute were found.")
    
    return {
        'statusCode': 200,
        'body': terminated_instances
    }
