import boto3
import os


bucket = os.environ.get('BUCKET_NAME')
region_name=os.environ.get('REGION')
use_ssl=True
endpoint_url=os.environ.get('SCW_ENDPOINT_URL')
scw_access_key_id=os.environ.get('ACCESS_KEY_ID')
scw_secret_access_key=os.environ.get('ACCESS_KEY_SECRET')


def s3_client():
    return boto3.resource(
        's3',
        region_name=region_name,
        use_ssl=use_ssl,
        endpoint_url=endpoint_url,
        aws_access_key_id=scw_access_key_id,
        aws_secret_access_key=scw_secret_access_key
    )

def save_to_bucket(filename: str, file_content: str):
    client = s3_client()
    
    obj = client.Object(bucket, filename)
    obj.put(
        Body=file_content
    )
