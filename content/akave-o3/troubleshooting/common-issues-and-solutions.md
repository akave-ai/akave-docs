---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Common Issues and Solutions'
weight: 19
cascade:
  type: docs
---

This page lists known issues when using the AWS CLI (`s3api` and `s3`) with Akave O3 and provides tested workarounds or solutions.

## Issue: Uploads fail due to checksum validation headers (AWS CLI v2.23.0+)

### Error:

An error occurred (InvalidArgument) when calling the PutObject operation: Unsupported header 'x-amz-sdk-checksum-algorithm' received for this API call.

### Cause:

In AWS CLI v2.23.0+ and v1.37.0+, `aws s3 cp` and `aws s3api put-object` **automatically include checksum headers** like `x-amz-sdk-checksum-algorithm` and `x-amz-checksum-crc64nvme`, even when not required.

This behavior breaks compatibility with third-party S3-compatible endpoints like Akave O3.

### Workaround 1: Downgrade AWS CLI

Use a known working version such as:

- AWS CLI v2.22.35 or older
- AWS CLI v1.36.40 or older

Run:
```bash
aws --version
```
### Workaround 2: Update config file

In `~/.aws/config`, add the following under your O3 profile:
```bash
[profile o3]  
region = akave-network  
request_checksum_calculation = WHEN_REQUIRED  
response_checksum_validation = WHEN_REQUIRED
```
Then use the profile in your commands:
```bash
aws s3 cp ./file.txt s3://my-akave-bucket/ \
  --profile o3 \
  --endpoint-url https://o3-rc1.akave.xyz
```
### Workaround 3: Explicitly specify a supported checksum (e.g., CRC32)
```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key example.txt \
  --body ./example.txt \
  --checksum-algorithm CRC32 \
  --endpoint-url https://o3-rc1.akave.xyz
```
### Why this matters:

Versions between 2.23.0 and 2.23.5 (and 1.37.0 in CLI v1) are **not compatible** with Akave or many third-party S3 APIs unless configuration is modified or CLI is updated.

## Issue: Downloading Versioned Files from O3 Results in Directory Structure

### Error:

If you are running a self-hosted instance of Akave O3 and enable bucket versioning, the object names in the Akave Network include version tags appended to them. 

For example for an object file.txt:
- file.txt/null
- file.txt/V1
- file.txt/V2
- etc.

When downloading the file using the akavecli, the file will be downloaded with the version tag as the file name, while the file name is the name of the directory.

For example after downloading:

```shell
cd file.txt
```
Shows a directory containing the version tag:

```shell
V1
```

### Cause:

The akavecli interprets the value following a "/" character as a directory, so it creates a directory with the name of the file and downloads the file into it.

### Workaround:

If you want to download this file using the akavecli, you must follow these steps:

1. Create a directory with your file name
```shell
mkdir file.txt
```
1. Perform the download using the akavecli
```shell
akavecli ipc file download <bucket-name> file.txt/null . --node-address=connect.akave.ai:5500 --private-key "your-private-key"
```
> This will create a file inside your new directory named `null`, `V1`, `V2` or whatever version it is, and `your-private-key` in this case is the private key used for your O3 instance.
1. Move into that directory
```shell
cd file.txt
```
1. Rename the downloaded file (e.g., null, V1, etc.) to a temporary name and move it up one level
```shell
mv * ../file.tmp
```
1. Return to the parent directory and remove the temporary directory
```shell
cd ..
rmdir file.txt
```
1. Rename the file back to it's original file name (file.txt in this example)
```shell
mv file.tmp file.txt
```


## Still having issues?

Try adding `--debug` to your command and refer to the [Debugging S3 Requests](../debugging-s3-requests/) section.