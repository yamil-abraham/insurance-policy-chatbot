import pickle
import os
import boto3
from config import DOWNLOAD_PATH, ACCESS_KEY, SECRET_KEY, BUCKET_NAME, prefix


def download_data():
    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    # List the objects in the bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)

    # Download the objects
    for obj in response['Contents']:
        key = obj['Key']
        if key.endswith('.pdf'):
            file_name = os.path.join(DOWNLOAD_PATH, os.path.basename(key))
            s3.download_file(BUCKET_NAME, key, file_name)
            print(f"Download {key} as {file_name}")


# Check if there are existing files in the DOWNLOAD_PATH
if not os.listdir(DOWNLOAD_PATH):
    download_data()