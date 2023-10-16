import logging
import psycopg2

# The Below code contains hardcoded credentials and should be reporded in the problems console

# insert AWS credentials with righ size of the string
AWS_ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AWS_REGION = 'us-east-1'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="XXXXXXXX",
        password="XXXXXXXX"
    )

# CWE-798 - Hardcoded credentials: Access credentials, such as passwords and access keys, 
# should not be hardcoded in source code. 
# Hardcoding credentials may cause leaks even after removing them. 
# This is because version control systems might retain older versions of the code. 
# Credentials should be stored securely and obtained from the runtime environment.
