import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Specify the instance IDs of the EC2 instances you want to stop
    instance_ids = ['instance_id_1', 'instance_id_2']  # Add more instance IDs as needed

    # Stop the EC2 instances
    response = ec2.stop_instances(InstanceIds=instance_ids)

    # Print the response
    print(response)

    # Optionally, you can return a response to indicate success or failure
    return {
        'statusCode': 200,
        'body': 'EC2 instances stopped successfully.'
    }
