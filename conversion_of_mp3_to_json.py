import json
import boto3

s3 = boto3.resource('s3')
s3_client=boto3.client('s3')
client = boto3.client('transcribe')

def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    bucketname = event['Records'][0]['s3']['bucket']['name']
    source_bucket = s3.Bucket('sainath-output-file')
    dest_bucket = s3.Bucket('sainath-json-bucket')
    
    def obj_last_modified(myobj):
        return myobj.last_modified
        
    sortedObjects = sorted(source_bucket.objects.all(), key=obj_last_modified, reverse=True)
    print(sortedObjects[0].key)
    o = sortedObjects[0].key
    
    # response_contents = s3_client.list_objects_v2(
    #     Bucket='sainath-output-file'
    #     )
    # print(response_contents['Contents'][0]['Key'])
    # var = response_contents['Contents'][0]['Key']
    
    client.start_transcription_job(
        TranscriptionJobName=o,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': 's3://sainath-output-file/' + o,
        },
        OutputBucketName='sainath-json-bucket',
        OutputKey=o.strip('.mp3') +'.json',
    )
    # s3.Object(source_bucket.name, response_contents['Contents'][0]['Key']).delete()    