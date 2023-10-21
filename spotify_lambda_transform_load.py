import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucket = "spotify-etl-proj-wl"
    Key = "raw_data/to_processed/"
    
    for file in s3.list_objects(Bucket = Bucket, Prefix=Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1] == 'json':
            response = s3.get_object(Bucket=Bucket, Key=file_key)
            content = response['Body']
            jsonObj = json.loads(content.read())
            print(jsonObj)