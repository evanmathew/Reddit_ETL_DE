import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY


def connect_to_s3():
    """
    Connects to AWS S3 service using the provided credentials.

    Returns:
        s3fs.S3FileSystem: An instance of the S3FileSystem class.
    """

    try:
        # Create an S3FileSystem instance using the provided credentials
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_ACCESS_KEY
        )

        return s3

    except Exception as e:
        # Print the exception message if any error occurs
        print(e)




def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str) -> None:
    """
    Creates a bucket in S3 if it does not already exist.

    Args:
        s3 (s3fs.S3FileSystem): The S3FileSystem instance.
        bucket (str): The name of the bucket to be created.

    Returns:
        None
    """
    try:
        # Check if the bucket already exists
        if not s3.exists(bucket):
            # If not, create the bucket
            s3.mkdir(bucket)
            print("Bucket created")
        else:
            print("Bucket already exists")
    except Exception as e:
        # Print any exceptions that occur
        print(e)





def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket:str, s3_file_name: str):
    """
    Uploads a file to S3.

    Args:
        s3 (s3fs.S3FileSystem): The S3FileSystem instance.
        file_path (str): The local path of the file to be uploaded.
        bucket (str): The name of the S3 bucket.
        s3_file_name (str): The name of the file in the S3 bucket.

    Returns:
        None
    """
    try:
        # Upload the file to S3
        s3.put(file_path, bucket+'/raw/'+ s3_file_name) # it will upload to raw folder (bucket/raw/s3_file_name)
        print('File uploaded to s3')
    except FileNotFoundError:
        # Print an error message if the file is not found
        print('The file was not found')
