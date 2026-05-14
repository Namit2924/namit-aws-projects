import boto3
import os

# Your bucket name
BUCKET_NAME = "namit-static-site-2026"

# Local website folder
WEBSITE_DIR = "my-website"

# Create S3 client
s3 = boto3.client('s3')

# Function to upload files
def upload_files():
    for root, dirs, files in os.walk(WEBSITE_DIR):
        for file in files:
            local_path = os.path.join(root, file)
            
            # S3 path
            s3_path = os.path.relpath(local_path, WEBSITE_DIR).replace("\\", "/")
            
            print(f"Uploading {s3_path}...")

            # Upload file
            s3.upload_file(
                local_path,
                BUCKET_NAME,
                s3_path,
                ExtraArgs={'ContentType': get_content_type(file)}
            )

# Set content type for files
def get_content_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    elif filename.endswith(".css"):
        return "text/css"
    elif filename.endswith(".js"):
        return "application/javascript"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    else:
        return "binary/octet-stream"

if __name__ == "__main__":
    upload_files()
    print("✅ Upload complete!")