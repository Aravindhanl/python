import boto3

client = boto3.client('iam',aws_access_key_id='AKIA2SITOGADH77K57M5',aws_secret_access_key='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', 
                      region_name= 'us-east-1')

response = client.list_access_keys(
    UserName = 'aravind',
)

#print(response)

for acs in response['AccessKeyMetadata']:
   # print(acs.get('AccessKeyId'),acs.get('Status'))
    AccessKey=acs.get('AccessKeyId')
    status=acs.get('Status')
iam = boto3.client('iam')
activate_key= iam.update_access_key(
    AccessKeyId=str(AccessKey)
    Status='Active',
    #Status='Inactive'
    #Status='Active'
)
print(activate_key)
