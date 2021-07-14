import boto3
import os

client = boto3.client('ec2',aws_access_key_id='AKIA2SITOGADH77K57M5',aws_secret_access_key='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', 
                      region_name= 'us-east-1')
response = client.describe_images(
        Filters=[
        {
            'Name': 'state',
            'Values': [
                'failed',
            ]
        },
    ],
    ImageIds=[],
    Owners=[],
)
#print(response)
for doc in response['Images']:
    print(doc.get('ImageId'),doc.get('StateReason'))
