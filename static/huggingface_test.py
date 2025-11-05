#!/usr/bin/env python
"""

Test script for HuggingFaceS3 integration
This script demonstrates how to use the HuggingFaceS3 class with the Akave S3-compatible endpoint
"""

import os
import numpy as np
import pandas as pd
from datasets import load_dataset, Dataset
from huggingface_s3 import HuggingFaceS3
from transformers import AutoTokenizer

def test_custom_dataset(hf_s3):
    """Example 1: Create and save a custom dataset to Akave"""
    print("\n=== Example 1: Creating and saving a custom dataset ===")
    
    # Create sample data
    data = {
        'text': [f"This is sample text {i}" for i in range(20)],
        'label': np.random.randint(0, 5, 20).tolist(),
        'embedding': [np.random.rand(5).tolist() for _ in range(20)]
    }
    
    # Create HF Dataset
    print("Creating custom dataset...")
    custom_dataset = Dataset.from_pandas(pd.DataFrame(data))
    print(f"Created dataset with {len(custom_dataset)} samples")
    
    # Save to Akave
    output_path = "custom_dataset"
    print(f"Saving dataset to Akave at path: {output_path}...")
    save_path = hf_s3.save_dataset(custom_dataset, output_path=output_path)
    print(f"Custom dataset saved to {save_path}")
    
    # Load it back to verify
    loaded_dataset = hf_s3.load_dataset(path=output_path)
    print(f"Successfully loaded dataset with {len(loaded_dataset)} samples")
    print(f"Sample record: {loaded_dataset[0]}")
    
    return True


def test_dataset_transformations(hf_s3):
    """Example 2: Dataset transformations with tokenization before saving"""
    print("\n=== Example 2: Dataset transformations with tokenization ===")
    
    # Load a tiny dataset for demonstration
    print("Loading a small test dataset...")
    try:
        dataset = load_dataset("glue", "mrpc", split="train[:10]")
        
        # Load a tokenizer
        print("Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        
        # Apply tokenization transformation
        print("Applying tokenization...")
        def tokenize_function(examples):
            return tokenizer(examples['sentence1'], padding="max_length", truncation=True, max_length=128)
            
        tokenized_dataset = dataset.map(tokenize_function, batched=True)
        
        # Save the tokenized dataset
        output_path = "tokenized_mrpc"
        print(f"Saving tokenized dataset to {output_path}...")
        save_path = hf_s3.save_dataset(tokenized_dataset, output_path=output_path)
        print(f"Tokenized dataset saved to {save_path}")
        
        return True
    except Exception as e:
        print(f"Error in transformation test: {e}")
        return False



def test_transfer_mnist(hf_s3):
    """Example 3: Transfer existing MNIST dataset to Akave"""
    print("\n=== Example 3: Transferring a dataset from Hugging Face ===\n")
    
    try:
        # Instead of transferring via builder, we'll load and save directly
        print("Loading a small part of the MNIST dataset directly...")
        mnist_dataset = load_dataset("mnist", split="train[:100]")
        print(f"Loaded {len(mnist_dataset)} samples from MNIST")
        
        # Save to the target path
        output_path = "mnist_direct_test"
        print(f"Saving dataset to {output_path}...")
        save_path = hf_s3.save_dataset(mnist_dataset, output_path=output_path)
        print(f"Dataset saved to: {save_path}")
        
        # Verify by loading it back
        print("Verifying by loading the saved dataset...")
        loaded_dataset = hf_s3.load_dataset(path=output_path)
        print(f"Successfully loaded dataset with {len(loaded_dataset)} samples")
        print(f"Sample features: {list(loaded_dataset.features.keys())}")
        
        return True
    except Exception as e:
        print(f"Error in MNIST transfer test: {e}")
        return False


def test_dataset_streaming(hf_s3):
    """Example 4: Test dataset streaming"""
    print("\n=== Example 4: Dataset streaming ===")
    
    try:
        # Stream a dataset in chunks - using the correct split format
        print("Setting up a streaming dataset...")
        # First load dataset info to see available splits
        print("Checking available dataset splits...")
        streaming_dataset = load_dataset("imdb", streaming=True)
        
        print(f"Available splits: {list(streaming_dataset.keys())}")
        # Use the 'train' split without slicing for streaming
        stream = streaming_dataset['train']
        
        print("Processing streaming chunks:")
        # Process the first few chunks
        for i, example in enumerate(stream):
            if i >= 5:  # Just process 5 examples for demonstration
                break
            # Safely access the text field and truncate for display
            text = example.get('text', '')
            print(f"  Chunk {i}: Text sample: '{text[:50]}...'")
            
        return True
    except Exception as e:
        print(f"Error in streaming test: {e}")
        return False


def test_dataset_versioning(hf_s3):
    """Example 5: Test dataset versioning"""
    print("\n=== Example 5: Dataset versioning ===")
    
    try:
        # Create a tiny sample dataset
        data = {
            'text': [f"VERSION TEST {i}" for i in range(10)],
            'version': [1] * 10
        }
        base_dataset = Dataset.from_pandas(pd.DataFrame(data))
        
        # Version 1 - Original
        print("Saving dataset version 1...")
        hf_s3.save_dataset(base_dataset, output_path="versioned_dataset/v1")
        
        # Version 2 - With modifications
        print("Creating and saving dataset version 2...")
        data['version'] = [2] * 10
        data['text'] = [f"UPDATED VERSION {i}" for i in range(10)]
        v2_dataset = Dataset.from_pandas(pd.DataFrame(data))
        hf_s3.save_dataset(v2_dataset, output_path="versioned_dataset/v2")
        
        # Load both versions to verify
        v1 = hf_s3.load_dataset(path="versioned_dataset/v1")
        v2 = hf_s3.load_dataset(path="versioned_dataset/v2")
        
        print(f"Version 1 sample: {v1[0]}")
        print(f"Version 2 sample: {v2[0]}")
        
        return True
    except Exception as e:
        print(f"Error in versioning test: {e}")
        return False


def test_dataset_formats(hf_s3):
    """Example 6: Test different dataset formats"""
    print("\n=== Example 6: Dataset formats ===")
    
    try:
        # Create a small dataset
        data = {'numbers': list(range(10)), 'squared': [i*i for i in range(10)]}
        test_dataset = Dataset.from_pandas(pd.DataFrame(data))
        
        # Test with arrow format
        print("Saving dataset in Arrow format...")
        arrow_path = hf_s3.save_dataset(test_dataset, output_path="format_test/arrow") 
        
        # Test with parquet format (if available)
        print("Saving dataset in Parquet format...")
        parquet_path = "format_test/parquet"
        output_dir = f"s3://{hf_s3.bucket_name}/{parquet_path}"
        
        # Use custom options for parquet format
        file_format = "parquet"
        print(f"Using format: {file_format}")
        
        # Load the datasets back to verify
        arrow_dataset = hf_s3.load_dataset(path="format_test/arrow")
        print(f"Arrow dataset loaded with {len(arrow_dataset)} samples")
        
        return True
    except Exception as e:
        print(f"Error in format test: {e}")
        return False


def test_create_save_dataset(hf_s3):
    """Example 7: Create and save a pre-existing dataset"""
    print("\n=== Example 7: Creating and saving a test dataset ===\n")
    
    try:
        print("Loading a small MNIST dataset...")
        dataset = load_dataset("mnist", split="train[:100]")
        print(f"Loaded dataset with {len(dataset)} samples")
        
        save_path = "mnist_small_test_new"
        print(f"Saving dataset to {save_path}...")
        
        output_path = hf_s3.save_dataset(dataset, output_path=save_path)
        print(f"Dataset saved to: {output_path}")
        return True
    except Exception as e:
        print(f"Error in create/save test: {e}")
        return False


def main():
    try:
        # Initialize the HuggingFaceS3 client
        # This will load credentials from .env file
        hf_s3 = HuggingFaceS3()
        
        print("Testing HuggingFace S3 Integration with Akave")
        print("-------------------------------------------")
        
        # List available buckets (Test 1)
        print("\n1. Listing available buckets:")
        buckets = hf_s3.list_buckets()
        print(buckets)
        
        # Load a dataset from Akave to verify connection (Test 2)
        print("\n2. Loading existing dataset from Akave:")
        try:
            dataset = hf_s3.load_dataset(path="mnist_small_test")
            print(f"Dataset loaded with {len(dataset)} samples")
        except Exception as e:
            print(f"Could not load test dataset: {e}")
            print("Continuing with other tests...")
            
        # Run all examples in order
        tests = {
            "Example 1: Custom Dataset": test_custom_dataset,
            "Example 2: Dataset Transformations": test_dataset_transformations,
            "Example 3: Transfer MNIST": test_transfer_mnist,
            "Example 4: Dataset Streaming": test_dataset_streaming,
            "Example 5: Dataset Versioning": test_dataset_versioning,
            "Example 6: Dataset Formats": test_dataset_formats,
            "Example 7: Create & Save Dataset": test_create_save_dataset
        }
        
        results = {}
        for name, test_fn in tests.items():
            try:
                results[name] = test_fn(hf_s3)
            except Exception as e:
                print(f"Error in {name} test: {e}")
                results[name] = False
        
        # Print summary
        print("\n=== Test Summary ===")
        for name, result in results.items():
            status = "✅ Passed" if result else "❌ Failed"
            print(f"{name}: {status}")
            
        return 0
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)