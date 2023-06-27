import boto3
from time import sleep

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

#implement a function to create a simple dynomodb table
def create_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='my-first-table',
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
    return table

