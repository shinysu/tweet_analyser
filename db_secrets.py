import os

DB_NAME = os.getenv("pyskills_db", 'tweet_analyser')
USER_NAME = "root"
PASSWORD = os.getenv('db_password', "")
HOST = "localhost"
