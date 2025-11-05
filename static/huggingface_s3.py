#!/usr/bin/env python
"""
Hugging Face integration with Akave's S3-compatible endpoints.
This script provides functions to interact with Hugging Face datasets using Akave's S3-compatible storage.
"""

import os
import s3fs
from pathlib import Path
from dotenv import load_dotenv
from datasets import load_dataset_builder, load_from_disk

# Load environment variables from .env file
def load_env_file(env_path=None):
    """Load environment variables from .env file
    
    Args:
        env_path (str, optional): Path to the .env file. If None, looks in current directory.
        
    Raises:
        FileNotFoundError: If .env file doesn't exist
    """
    if env_path is None:
        env_path = '.env'
    
    env_file = Path(env_path)
    if not env_file.exists():
        raise FileNotFoundError(f"Required .env file not found: {env_path}")
        
    load_dotenv(dotenv_path=env_path)


class HuggingFaceS3:
    """
    A class to manage Hugging Face datasets with S3-compatible storage.
    """
    
    def __init__(self, env_file='.env'):
        """
        Initialize the HuggingFaceS3 client.
        
        Args:
            env_file (str): Path to .env file containing configuration. Default is '.env' in current directory.
            
        Raises:
            FileNotFoundError: If .env file doesn't exist
            ValueError: If required credentials are not found in the .env file
        """
        # Load credentials from .env file
        load_env_file(env_file)
            
        # Get required credentials from environment variables
        self.access_key = os.environ.get('AKAVE_ACCESS_KEY')
        self.secret_key = os.environ.get('AKAVE_SECRET_KEY')
        self.endpoint_url = os.environ.get('AKAVE_ENDPOINT_URL')
        self.bucket_name = os.environ.get('AKAVE_BUCKET_NAME')
        
        # Validate required credentials
        if not self.access_key:
            raise ValueError("AKAVE_ACCESS_KEY not found in .env file")
        if not self.secret_key:
            raise ValueError("AKAVE_SECRET_KEY not found in .env file")
        if not self.endpoint_url:
            raise ValueError("AKAVE_ENDPOINT_URL not found in .env file")
        if not self.bucket_name:
            raise ValueError("AKAVE_BUCKET_NAME not found in .env file")
            
        # Set up the S3 file system
        self.storage_options = {
            "key": self.access_key,
            "secret": self.secret_key,
            "client_kwargs": {
                'endpoint_url': self.endpoint_url
            }
        }
        
        self.fs = s3fs.S3FileSystem(**self.storage_options)
        
    def list_buckets(self):
        """
        List available buckets.
        
        Returns:
            list: List of bucket names.
        """
        return self.fs.ls("")
    
    def get_s3_path(self, bucket_name=None, path=""):
        """
        Generate a valid S3 path.
        
        Args:
            bucket_name (str, optional): Bucket name. Defaults to the instance's bucket_name.
            path (str, optional): Path within the bucket.
            
        Returns:
            str: Formatted S3 path.
        """
        bucket = bucket_name or self.bucket_name
        if not bucket:
            raise ValueError("Bucket name must be provided")
        
        # Ensure path doesn't start with a slash
        if path and path.startswith('/'):
            path = path[1:]
            
        return f"s3://{bucket}/{path}"
        
    def transfer_dataset(self, dataset_name, bucket_name=None, output_path=None, file_format="parquet"):
        """
        Transfer an existing Hugging Face dataset to S3 storage.
        
        Args:
            dataset_name (str): Name of the dataset on Hugging Face Hub.
            bucket_name (str, optional): Bucket name to store the dataset in.
            output_path (str, optional): Path within the bucket. If None, uses dataset_name.
            file_format (str, optional): Format to save the dataset in. Defaults to "parquet".
            
        Returns:
            str: Path where the dataset was saved.
        """
        builder = load_dataset_builder(dataset_name)
        
        # Set up output directory
        output_dir = self.get_s3_path(
            bucket_name=bucket_name,
            path=output_path or dataset_name
        )
        
        print(f"Transferring dataset {dataset_name} to {output_dir}")
        builder.download_and_prepare(
            output_dir,
            storage_options=self.storage_options,
            file_format=file_format
        )
        
        return output_dir
    
    def save_dataset(self, dataset, bucket_name=None, output_path=None):
        """
        Save a dataset to S3 storage.
        
        Args:
            dataset: The dataset to save.
            bucket_name (str, optional): Bucket name to store the dataset in.
            output_path (str, optional): Path within the bucket.
            
        Returns:
            str: Path where the dataset was saved.
        """
        output_dir = self.get_s3_path(
            bucket_name=bucket_name,
            path=output_path
        )
        
        print(f"Saving dataset to {output_dir}")
        dataset.save_to_disk(output_dir, storage_options=self.storage_options)
        
        return output_dir
    
    def load_dataset(self, bucket_name=None, path=None):
        """
        Load a dataset from S3 storage.
        
        Args:
            bucket_name (str, optional): Bucket name where the dataset is stored.
            path (str): Path within the bucket.
            
        Returns:
            Dataset: The loaded dataset.
        """
        s3_path = self.get_s3_path(bucket_name=bucket_name, path=path)
        
        print(f"Loading dataset from {s3_path}")
        dataset = load_from_disk(s3_path, storage_options=self.storage_options)
        
        return dataset


# Example usage
if __name__ == "__main__":
    try:
        # Initialize client with .env file
        hf_s3 = HuggingFaceS3()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        exit(1)
    
    # List buckets
    print("Available buckets:")
    print(hf_s3.list_buckets())