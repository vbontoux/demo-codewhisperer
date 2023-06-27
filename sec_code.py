import logging
import psycopg2

# The Below code contains hardcoded credentials and should be reporded in the problems console

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="XXXXXXXX",
        password="XXXXXXXX"
    )

