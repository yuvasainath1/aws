import json
import boto3
import os

def lambda_handler(event, context):
    s3_client = boto3.client('ssm')
    response = s3_client.get_parameter(Name='bucketname')
    print(os.environ['access'])
    return{
        "statusCode": 200,
        "body":response['Parameter']['Value']
    }