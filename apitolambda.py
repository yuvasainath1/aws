import json
import boto3
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
cs_client = boto3.client('cloudsearchdomain',endpoint_url='http://doc-thor-itorjfeh3t6hn5izaqycirkjza.us-east-1.cloudsearch.amazonaws.com')
def lambda_handler(event, context):
    if (event['queryStringParameters'] != None ):
        if ( (event['queryStringParameters']['foo']!= None) and (event['queryStringParameters']['foo'][0]!= "")):
            q = event['queryStringParameters']['foo']
            print(q)
    r=cs_client.search(
        query=q
        )
    print(r)
    response =  {
                "statusCode": 200,
                "body": r['hits']['hit']
                # "headers": { "Access-Control-Allow-Origin": "*", "Content-Type": "application/json" }
                }
    print(response)