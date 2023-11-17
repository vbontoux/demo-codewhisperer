import boto3

# insert AWS credentials with righ size of the string
AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_REGION = 'us-east-1'


# create a function that connects to a database using pymysql 
# take user name and password as parameters and return a connection object    
import pymysql
def connect_to_db(user, password):
    conn = pymysql.connect(
        host="localhost",
        database="postgres",
        user=user,
        password=password
    )
    return conn