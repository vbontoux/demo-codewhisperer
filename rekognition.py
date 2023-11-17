import boto3
from time import sleep

# a function that use rekognition to  get the celebrity name an image in S3
def get_celebrity_name(file_name):
    rekognition = boto3.client("rekognition")
    response = rekognition.recognize_celebrities(
        Image={
            "S3Object": {
                "Bucket": "bontov-celebrities",
                "Name": file_name,
            }
        }
    )
    print(response["CelebrityFaces"][0]["Name"])
        

get_celebrity_name("images-2.jpeg")


