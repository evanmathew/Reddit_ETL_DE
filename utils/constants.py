import configparser # for reading config file
import os  

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf')) # reading all of credentials from ./config/config.conf

#REDDIT API KEYS
SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

#DATABASE(POSTGRES) CREDENTIALS 
DATABASE_HOST =  parser.get('database', 'database_host')
DATABASE_NAME =  parser.get('database', 'database_name')
DATABASE_PORT =  parser.get('database', 'database_port')
DATABASE_USER =  parser.get('database', 'database_username')
DATABASE_PASSWORD =  parser.get('database', 'database_password')

#AWS CREDENTIALS
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

#DATA STORING FILE-PATH
INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path') #filepath and outpath is defined in config/config.conf


# Required coloumns needed from reddit post data
POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)