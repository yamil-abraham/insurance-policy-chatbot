import pickle
import os
import boto3


# Configure the download path
DOWNLOAD_PATH = 'database/queplan_insurance'
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# Configure the AWS credentials
ACCESS_KEY = 'AKIA2JHUK4EGBAMYAYFY'
SECRET_KEY = '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'
DATASET_PATH = 's3://anyoneai-datasets/queplan_insurance/'
BUCKET_NAME = "anyoneai-datasets"
prefix = "queplan_insurance/"

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
