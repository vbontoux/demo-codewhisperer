import boto3
from time import sleep

# Examples of AWS API code using boto3

# function to upload a file to S3 using server side encryption
def upload_file_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ServerSideEncryption': 'AES256'})

    return response


# fucntion that transcribes a french audio file to text
def transcribe_file(file_name):
    transcribe = boto3.client("transcribe")
    transcribe.start_transcription_job(
        TranscriptionJobName="my-first-transcription-job",
        Media={"MediaFileUri": file_name},
        MediaFormat="mp3",
        LanguageCode="fr-FR",
    )
    # wait for the job to finish
    while True:
      status = transcribe.get_transcription_job(TranscriptionJobName="my-first-transcription-job")
      # wait 1 second before checking again
      sleep(1)
      if status["TranscriptionJob"]["TranscriptionJobStatus"] in ["COMPLETED", "FAILED",]:
        break
    
    # print the result text
    print(status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"])

# This one allows you to chose various code samples with different licences (MIT, Apache ...). This will add a log into the CodeWhisperer console.
# implement a function to create a simple dynomodb table
def create_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print(table)