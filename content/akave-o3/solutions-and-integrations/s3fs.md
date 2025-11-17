---
date: '2025-04-23T22:48:28-05:00'
draft: false
title: 'S3FS'
weight: 31
cascade:
  type: docs
---

[S3FS](https://s3fs.readthedocs.io/en/latest/) is a library built on top of botocore that allows you to mount Akave storage as a local file system while preserving the native object format for files.

The [s3fs-fuse](https://github.com/s3fs-fuse/s3fs-fuse) driver is a user-space file system that provides a virtual file system interface to S3-compatible storage. It allows you to access your Akave storage as a local file system, making it easy to work with your data as if it were stored on your local machine.

## Prerequisites

- **Akave Cloud Credentials**  
These can be requested by contacting Akave at [Akave Cloud Contact](https://www.akave.cloud/contact).

- **Install dependencies** (Requirements: Python 3.9+, pip, s3fs)

## Installation

{{< callout type="info" >}}
**Note on Python commands:** Throughout this guide, we provide commands for default Python 3 installations  using `python` and `pip`. For systems where you need to explicitly specify Python 3 you may need to use `python3` and `pip3`. Use the command variation that works for your specific environment.
{{< /callout >}}

### Pip Installation Instructions

Pip comes pre-installed with Python 3.4 and later. If you don't already have Python installed, you can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

You can verify that pip is installed by running the following command:

```bash
pip --version
```

### S3FS Installation Instructions

The simplest way to install the S3FS library is to use pip:

```bash
pip install s3fs
```

Run the following command to verify installation:

```bash
pip show s3fs
```

### S3FS Fuse Installation Instructions

#### MacOS
macOS 10.12 and newer via Homebrew:

```bash
brew install --cask macfuse
brew install gromgit/fuse/s3fs-mac
```

#### Linux
Debian 9 and Ubuntu 16.04 or newer:

```bash
sudo apt install s3fs
```

## Authentication

Before using S3FS with Akave, you need to configure authentication. There are several ways to do this, for this guide we'll focus on those that use the default AWS CLI profile functionality.

For more information on using the AWS CLI with Akave O3 see the documentation on [setup](/akave-o3/introduction/setup/).

For other authentication methods see the [S3FS Fuse Github](https://github.com/s3fs-fuse/s3fs-fuse).

#### Option 1: Credentials File

Create or edit `~/.aws/credentials` and add your Akave credentials:

```ini
[akave-o3]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
endpoint_url = https://o3-rc2.akave.xyz
```

#### Option 2: AWS CLI
Run the below command and follow the prompts to add your access key, secret key, and region.

```bash
aws configure --profile akave-o3
```
- AWS Access Key ID: `<your_access_key>`
- AWS Secret Access Key: `<your_secret_key>`
- Default region name: `akave-network`
- Default output format: `json`

## Usage

### CLI (s3fs-fuse)

#### Mounting an Akave Bucket

**Create a directory to mount your bucket**
```bash
mkdir -p ~/akave-mount
```

**Mount the bucket**
```bash
s3fs your-bucket-name ~/akave-mount \
  -o url=https://o3-rc2.akave.xyz \
  -o profile=akave-o3
```

**Check active mounts**
```bash
mount | grep s3fs
```

**Unmount when done**
```bash
umount ~/akave-mount
```

#### Additional mounting options

**Enable Debugging**
```bash
-o dbglevel=info -f
```
*The `-f` flag is used to run s3fs in foreground mode, which is useful for debugging.*

To modify the verbosity of the output, use `dbglevel=` followed by one of the following:

- debug
- warn
- info
- err

**Use Cache**
```bash
-o use_cache=/path/to/cache
```
Specifies a directory to use for caching files.

**Parallel Upload**
```bash
-o parallel_count=1       
```
Controls the number of parallel upload threads.

**Multi-Request Maximum**
```bash
-o multireq_max=1
```
Controls the maximum number of requests that can be made in parallel.

#### Basic Operations

Once mounted, you can use standard file system commands:

**List files in bucket with their sizes**
```bash
ls -l ~/akave-mount
```

**Copy a local file to the bucket**
```bash
cp myfile.txt ~/akave-mount/
```

**Download a file from the bucket**
```bash
cp ~/akave-mount/myfile.txt ./
```

**Delete a file from the bucket**
```bash
rm ~/akave-mount/myfile.txt
```

#### S3FS Specific Operations 

**Edit a file in place**
```bash
nano ~/akave-mount/notes/todo.txt
```

**View S3FS Logs** 

On MacOS:
```bash
log show --predicate 'process == "s3fs"' --last 1h
```

On Linux:
```bash
journalctl -t s3fs --since "1 hour ago"
```

### Python 

The S3FS Python library provides a powerful interface to work with Akave O3 storage programmatically. Below are examples of common operations and best practices.

#### Imports

To use S3FS in Python, you need to import the `s3fs` module:

```python
import s3fs
```

Some other imports that are helpful are OS for environment variables and pandas for data analysis.

```python
import os
import pandas as pd
```

#### Authentication Options

{{< callout type="warning" >}}
**Note:** Never hardcode credentials in your code, instead use one of the secure methods outlined below.
{{< /callout >}}

The below sections outline different ways to securely authenticate with Akave O3 storage using S3FS.

**Using Environment Variables**

Environment variables are a secure way to handle credentials. You can load them directly by exporting them in your shell:

```bash
export AKAVE_ACCESS_KEY=your_access_key_here
export AKAVE_SECRET_KEY=your_secret_key_here
```

Then in your Python code you can reference the credentials:

```python
import os

access_key = os.environ.get("AKAVE_ACCESS_KEY")
secret_key = os.environ.get("AKAVE_SECRET_KEY")

fs = s3fs.S3FileSystem(
    key=access_key,
    secret=secret_key,
    endpoint_url="https://o3-rc2.akave.xyz",
    client_kwargs={"region_name": "akave-network"}
)
```

**Using .env Files**

For development environments, you can use .env files with python-dotenv:

Example `.env` file:
```
AKAVE_ACCESS_KEY=your_access_key_here
AKAVE_SECRET_KEY=your_secret_key_here
```

Then in your Python code you can load the credentials from the .env file:
```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

fs = s3fs.S3FileSystem(
    key=os.environ.get("AKAVE_ACCESS_KEY"),
    secret=os.environ.get("AKAVE_SECRET_KEY"),
    endpoint_url="https://o3-rc2.akave.xyz",
    client_kwargs={"region_name": "akave-network"}
)
```

{{< callout type="warning" >}}
Make sure to add your `.env` file to `.gitignore` to prevent accidentally committing credentials to version control.
{{< /callout >}}

**Using AWS CLI Profile**

You may also use AWS CLI profiles, where credentials are stored in your system's credential store:

```python
fs = s3fs.S3FileSystem(
    profile="akave-o3",
    endpoint_url="https://o3-rc2.akave.xyz",
    client_kwargs={"region_name": "akave-network"}
)
```

#### Basic Operations

**List buckets**
```python
buckets = fs.ls("")
print(f"Available buckets: {buckets}")
```

**List files in a bucket**
```python
files = fs.ls("your-bucket-name")
for file in files:
    print(file)
```

**Create a directory**
```python
fs.mkdir("your-bucket-name/new-directory")
```

**Upload a file**
```python
fs.put("local-file.txt", "your-bucket-name/remote-file.txt")
```

**Upload a large file with progress tracking**
```python
with fs.open("your-bucket-name/large-file.zip", "wb") as remote_file:
    with open("local-large-file.zip", "rb") as local_file:
        remote_file.write(local_file.read())
        print("Upload complete!")
```

**Download a file**
```python
fs.get("your-bucket-name/remote-file.txt", "downloaded-file.txt")
```

**Download a large file in chunks**
```python
with fs.open("your-bucket-name/large-file.csv", "rb") as remote_file:
    # Process the file in chunks to avoid loading it all into memory
    chunk_size = 1024 * 1024  # 1 MB chunks
    while True:
        chunk = remote_file.read(chunk_size)
        if not chunk:
            break
        # Process chunk here
```

**Delete a file**
```python
fs.rm("your-bucket-name/file-to-delete.txt")
```

**Delete multiple files**
```python
fs.rm(["your-bucket-name/file1.txt", "your-bucket-name/file2.txt"])
```

**Delete a directory and all its contents recursively**
```python
fs.rm("your-bucket-name/directory-to-delete", recursive=True)
```

#### Working with Pandas

S3FS integrates well with pandas for data analysis workflows:

**Read CSV directly from Akave storage**
```python
df = pd.read_csv(fs.open("your-bucket-name/data.csv"))
```

**Write DataFrame back to Akave storage as CSV**
```python
df.to_csv(fs.open("your-bucket-name/processed-data.csv", "w"))
```

**Read parquet files directly from Akave storage**
```python
df = pd.read_parquet(fs.open("your-bucket-name/data.parquet"))
```

**Write DataFrame back to Akave storage as parquet**
```python
df.to_parquet(fs.open("your-bucket-name/processed-data.parquet", "wb"))
```

#### Advanced Operations

**Get file metadata and info**
```python
info = fs.info("your-bucket-name/myfile.txt")
print(f"File size: {info['size']} bytes")
print(f"Last modified: {info['LastModified']}")
```

**Copy objects within storage**
```python
fs.copy("your-bucket-name/source.txt", "your-bucket-name/destination.txt")
```

#### Error Handling and Best Practices

**Error handling**

Use try/except blocks to handle errors by checking the error code and handling it accordingly.

```python
import botocore.exceptions

try:
    # Attempt to access a file
    with fs.open("your-bucket-name/may-not-exist.txt", "rb") as f:
        content = f.read()
except botocore.exceptions.ClientError as e:
    if e.response["Error"]["Code"] == "NoSuchKey":
        print("The file does not exist")
    elif e.response["Error"]["Code"] == "AccessDenied":
        print("Access denied - check permissions")
    else:
        print(f"Error occurred: {e}")
```

**Batch operations for better performance**

Use batch operations to upload multiple files at once for better performance.

```python
files_to_upload = [
    ("local1.txt", "your-bucket-name/remote1.txt"),
    ("local2.txt", "your-bucket-name/remote2.txt"),
    ("local3.txt", "your-bucket-name/remote3.txt")
]

for local, remote in files_to_upload:
    fs.put(local, remote)
```

**Connection pooling for multiple operations**

Use the same S3FileSystem instance for multiple operations to benefit from connection pooling by setting the `max_pool_connections` parameter.

```python
fs = s3fs.S3FileSystem(
    profile="akave-o3",
    endpoint_url="https://o3-rc2.akave.xyz",
    config_kwargs={"max_pool_connections": 20}
)
```

**Caching configuration**

Enable client-side caching to reduce the number of requests made to Akave storage by setting the `use_listings_cache` and `listings_expiry_time` parameters.

```python
fs = s3fs.S3FileSystem(
    profile="akave-o3",
    endpoint_url="https://o3-rc2.akave.xyz",
    use_listings_cache=True,
    listings_expiry_time=300  # Cache TTL in seconds
)
```

### Example Python Script

An example script demonstrating S3FS operations with Akave O3 is available in the [urandom](https://github.com/akave-ai/urandom) repository on the [Akave GitHub page](https://github.com/akave-ai).

To use the script clone the repository and navigate to the s3fs directory:

```bash
git clone https://github.com/akave-ai/urandom.git
cd urandom/s3fs
```

This script includes:
- **Bucket operations**: List buckets and their contents
- **File operations**: Upload, download, delete, and copy files
- **Directory operations**: Create directories and manage folder structures
- **Pandas integration**: Read and write DataFrames directly to/from Akave storage
- **Error handling**: Robust error handling patterns
- **CLI interface**: Command-line arguments for flexible testing

#### Dependencies

**Required packages (install via pip):**
- `s3fs`: Python library for S3-compatible object storage file system operations
- `pandas`: Data analysis library for working with DataFrames and structured data

**Standard library modules (included with Python):**
- `os`: Operating system interface for file operations
- `datetime`: Date and time handling
- `argparse`: Command-line argument parsing

**Install dependencies:**
```bash
pip install s3fs pandas
```

#### Usage examples

You can run the script with the following commands to run all tests or test specific operations with variable bucket and file names.

**Run all tests on a bucket:**
```bash
python s3fs_test.py my-bucket
```

**List buckets and contents:**
```bash
python s3fs_test.py my-bucket --operation list
```

**Upload a specific file:**
```bash
python s3fs_test.py my-bucket --operation upload --file data.csv
```

**Download a specific file:**
```bash
python s3fs_test.py my-bucket --operation download --file data.csv
```

**Delete a specific file:**
```bash
python s3fs_test.py my-bucket --operation delete --file data.csv
```

**Note:** The script uses the AWS CLI profile `akave-o3` by default. Modify the `create_s3fs_client()` function to use your configured profile name (e.g., `akave-o3`) or to use environment variables for authentication using the `key` and `secret` parameters described in the [Authentication](#authentication) section above