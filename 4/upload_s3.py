import boto3
import os

# Your bucket name
BUCKET_NAME = "namit-automation-bucket-2026"

# Local folder path
FOLDER_PATH = "my-files"

# Create S3 client
s3 = boto3.client('s3')

def upload_files():
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = file

            try:
                s3.upload_file(local_path, BUCKET_NAME, s3_path)
                print(f"✅ Uploaded: {file}")
            except Exception as e:
                print(f"❌ Failed: {file}", e)

upload_files()