from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    """
    Upload a file to AWS S3 bucket
    The file path is expected to be in the XCOM context
    """
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value') # getting the file path from previous task in AIRFLOW-WEBSERVER

    # Connect to S3 using credentials
    s3 = connect_to_s3()
    
    # Create the bucket if it doesn't exist
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    
    # Upload the csv file to S3 bucket
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1]) #name of the file is the last part of the file path
