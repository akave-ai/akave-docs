#!/usr/bin/env python3
"""
S3FS Test Script for Akave O3


This script demonstrates common S3FS operations using the AWS CLI profile "akave-o3"
for authentication. It provides examples of listing, uploading, downloading, and
other operations with Akave O3 storage.
"""


import os
from s3fs import S3FileSystem
import pandas as pd
from datetime import datetime
import argparse


def create_s3fs_client():
    """Initialize and return an S3FS client using the akave-o3 profile."""
    return S3FileSystem(
        profile="akave-o3",
        endpoint_url="https://o3-rc2.akave.xyz"
    )


def list_buckets(fs):
    """List all accessible buckets."""
    print("\n=== LISTING BUCKETS ===")
    buckets = fs.ls("")
    print(f"Found {len(buckets)} buckets:")
    for bucket in buckets:
        print(f"- {bucket}")
    
    return buckets


def list_bucket_contents(fs, bucket_name):
    """List contents of a specific bucket."""
    print(f"\n=== LISTING CONTENTS OF BUCKET: {bucket_name} ===")
    try:
        files = fs.ls(bucket_name)
        print(f"Found {len(files)} items:")
        for file in files:
            # Get file info
            info = fs.info(file)
            size_kb = info.get('size', 0) / 1024
            last_modified = info.get('LastModified', 'Unknown')
            if isinstance(last_modified, datetime):
                last_modified = last_modified.strftime('%Y-%m-%d %H:%M:%S')
            
            # Show file details
            print(f"- {file} ({size_kb:.2f} KB, modified: {last_modified})")
        return files
    except Exception as e:
        print(f"Error listing bucket contents: {e}")
        return []


def create_directory(fs, bucket_name, directory_name):
    """Create a directory in the specified bucket."""
    path = f"{bucket_name}/{directory_name}"
    print(f"\n=== CREATING DIRECTORY: {path} ===")
    try:
        fs.mkdir(path)
        print(f"Directory created successfully: {path}")
        return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False


def upload_file(fs, local_file, bucket_name, remote_path=None):
    """Upload a local file to the bucket."""
    if not os.path.exists(local_file):
        print(f"Local file not found: {local_file}")
        return False
    
    if remote_path is None:
        remote_path = f"{bucket_name}/{os.path.basename(local_file)}"
    else:
        remote_path = f"{bucket_name}/{remote_path}"
    
    print(f"\n=== UPLOADING FILE: {local_file} -> {remote_path} ===")
    try:
        fs.put(local_file, remote_path)
        print(f"File uploaded successfully: {remote_path}")
        
        # Verify upload
        info = fs.info(remote_path)
        size_kb = info.get('size', 0) / 1024
        print(f"Verified file size: {size_kb:.2f} KB")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False


def download_file(fs, bucket_name, remote_path, local_file=None):
    """Download a file from the bucket."""
    full_path = f"{bucket_name}/{remote_path}"
    if local_file is None:
        local_file = os.path.basename(remote_path)
    
    print(f"\n=== DOWNLOADING FILE: {full_path} -> {local_file} ===")
    try:
        fs.get(full_path, local_file)
        print(f"File downloaded successfully: {local_file}")
        
        # Verify download
        size_kb = os.path.getsize(local_file) / 1024
        print(f"Verified local file size: {size_kb:.2f} KB")
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False


def create_and_upload_test_file(fs, bucket_name, filename="test_file.txt"):
    """Create a test file and upload it to the bucket."""
    print("\n=== CREATING AND UPLOADING TEST FILE ===")
    
    # Create test content
    content = f"This is a test file created at {datetime.now().isoformat()}\n"
    content += "It was created by the s3fs_test.py script.\n"
    content += "=" * 40 + "\n"
    
    # Write to local file
    with open(filename, "w") as f:
        f.write(content)
    
    # Upload to bucket
    success = upload_file(fs, filename, bucket_name)
    
    # Clean up local file
    if os.path.exists(filename):
        os.remove(filename)
    
    return success


def delete_file(fs, bucket_name, remote_path):
    """Delete a file from the bucket."""
    full_path = f"{bucket_name}/{remote_path}"
    print(f"\n=== DELETING FILE: {full_path} ===")
    try:
        fs.rm(full_path)
        print(f"File deleted successfully: {full_path}")
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False


def read_file_content(fs, bucket_name, remote_path):
    """Read and display the content of a file in the bucket."""
    full_path = f"{bucket_name}/{remote_path}"
    print(f"\n=== READING FILE CONTENT: {full_path} ===")
    try:
        with fs.open(full_path, 'r') as f:
            content = f.read(8192)  # Read up to 8KB
            print("File content:")
            print("-" * 40)
            print(content)
            print("-" * 40)
        return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def create_pandas_dataset(fs, bucket_name):
    """Create a sample pandas DataFrame and save it to a CSV file in the bucket."""
    print("\n=== CREATING AND UPLOADING PANDAS DATASET ===")
    try:
        # Create a sample DataFrame
        data = {
            'id': range(1, 11),
            'name': [f'Item {i}' for i in range(1, 11)],
            'value': [i * 10.5 for i in range(1, 11)],
            'timestamp': [datetime.now().isoformat() for _ in range(10)]
        }
        df = pd.DataFrame(data)
        
        # Display the DataFrame
        print("Sample DataFrame:")
        print(df.head())
        
        # Save to CSV in the bucket
        csv_path = f"{bucket_name}/sample_data.csv"
        with fs.open(csv_path, 'w') as f:
            df.to_csv(f, index=False)
        print(f"DataFrame saved to CSV: {csv_path}")
        
        # Save to JSON in the bucket
        json_path = f"{bucket_name}/sample_data.json"
        with fs.open(json_path, 'w') as f:
            df.to_json(f, orient='records')
        print(f"DataFrame saved to JSON: {json_path}")
        
        return True
    except Exception as e:
        print(f"Error creating pandas dataset: {e}")
        return False


def read_pandas_dataset(fs, bucket_name, file_path="sample_data.csv"):
    """Read a CSV file from the bucket into a pandas DataFrame."""
    full_path = f"{bucket_name}/{file_path}"
    print(f"\n=== READING PANDAS DATASET: {full_path} ===")
    try:
        # Read the CSV file
        with fs.open(full_path, 'r') as f:
            df = pd.read_csv(f)
        
        # Display the DataFrame
        print("DataFrame from CSV:")
        print(df.head())
        print(f"Shape: {df.shape}")
        
        return df
    except Exception as e:
        print(f"Error reading pandas dataset: {e}")
        return None


def copy_object(fs, bucket_name, source_path, dest_path):
    """Copy an object within the same bucket."""
    source_full = f"{bucket_name}/{source_path}"
    dest_full = f"{bucket_name}/{dest_path}"
    print(f"\n=== COPYING OBJECT: {source_full} -> {dest_full} ===")
    try:
        fs.copy(source_full, dest_full)
        print(f"Object copied successfully")
        return True
    except Exception as e:
        print(f"Error copying object: {e}")
        return False


def run_all_tests(bucket_name):
    """Run all tests on the specified bucket."""
    fs = create_s3fs_client()
    
    # Basic operations
    buckets = list_buckets(fs)
    if bucket_name not in buckets:
        print(f"Warning: Bucket '{bucket_name}' not found in the list of available buckets.")
    
    list_bucket_contents(fs, bucket_name)
    create_directory(fs, bucket_name, "test_directory")
    create_and_upload_test_file(fs, bucket_name)
    read_file_content(fs, bucket_name, "test_file.txt")
    copy_object(fs, bucket_name, "test_file.txt", "test_directory/test_file_copy.txt")
    
    # Pandas operations
    create_pandas_dataset(fs, bucket_name)
    read_pandas_dataset(fs, bucket_name)
    
    # Clean up (uncomment if you want to delete test files)
    # delete_file(fs, bucket_name, "test_file.txt")
    # delete_file(fs, bucket_name, "test_directory/test_file_copy.txt")
    # delete_file(fs, bucket_name, "sample_data.csv")
    # delete_file(fs, bucket_name, "sample_data.json")
    
    print("\n=== ALL TESTS COMPLETED ===")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test S3FS operations with Akave O3")
    parser.add_argument("bucket", help="Bucket name to use for testing")
    parser.add_argument("--operation", choices=["list", "upload", "download", "delete", "all"], 
                        default="all", help="Specific operation to test (default: all)")
    parser.add_argument("--file", help="File path for upload/download operations")
    
    args = parser.parse_args()
    
    fs = create_s3fs_client()
    
    if args.operation == "list":
        list_buckets(fs)
        if args.bucket:
            list_bucket_contents(fs, args.bucket)
    elif args.operation == "upload" and args.file:
        upload_file(fs, args.file, args.bucket)
    elif args.operation == "download" and args.file:
        download_file(fs, args.bucket, args.file)
    elif args.operation == "delete" and args.file:
        delete_file(fs, args.bucket, args.file)
    elif args.operation == "all":
        run_all_tests(args.bucket)
    else:
        print("Invalid operation or missing required arguments")
        parser.print_help()
