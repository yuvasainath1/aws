import boto3
import json
import os

s3 = boto3.resource('s3')

def lambda_handler (event, context):
     s3_client = boto3.client('ssm')
     response = s3_client.get_parameter(Name='bucketname')
     bucket = s3.Bucket('sainathhh')
    #  dest_bucket=s3.Bucket(response['Parameter']['Value'])ssmparameter
     dest_bucket=s3.Bucket(os.environ['bucketname'])
     dest_bucket2=s3.Bucket('bucketu3')
     print(dest_bucket)
     print(bucket)
     print(os.environ['bucketname'])
     for obj in bucket.objects.all():
        dest_key=obj.key
        if obj.key.endswith('.pdf'):
            s3.Object(dest_bucket.name, dest_key).copy_from(CopySource= {'Bucket': obj.bucket_name, 'Key': obj.key})
            s3.Object(bucket.name, obj.key).delete()
        if obj.key.endswith('.docx'):
             s3.Object(dest_bucket2.name, dest_key).copy_from(CopySource= {'Bucket': obj.bucket_name, 'Key': obj.key})
             s3.Object(bucket.name, obj.key).delete()
