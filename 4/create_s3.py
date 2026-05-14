import boto3

# Create S3 client
s3 = boto3.client('s3')

# Unique bucket name (must be globally unique)
bucket_name = "namit-automation-bucket-2026"

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print(f"✅ Bucket '{bucket_name}' created successfully!")

except Exception as e:
    print("❌ Error:", e)