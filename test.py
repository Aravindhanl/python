import boto3
import json
import os
import datetime
import collections 
import smtplib 
import email.utils

from time import gmtime, strftime
from datetime import date, timedelta

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase  
from email import encoders

client = boto3.client('ec2',aws_access_key_id='AKIA2SITOGADH77K57M5',aws_secret_access_key='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', 
                      region_name= 'us-east-1')
response = client.describe_snapshots(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'error',
            ]
        },
    ],
    OwnerIds=[],
    SnapshotIds=[]
) 
#print(response['Snapshots'])
for doc in response['Snapshots']:
    #print(doc.get("VolumeId"), doc.get("StateMessage"))
    resultMsg = print(doc.get("VolumeId"),doc.get("StateMessage"))
   #print('The volume Ids': doc.get("VolumeId"), 'The state message': doc.get("StateMessage") )
today = date.today()
#today = datetime.datetime.now().strftime('%d-%m-%y')
#print(today)
print(resultMsg)