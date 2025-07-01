---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Generate and Use Presigned URLs'
weight: 9
cascade:
  type: docs
---

Akave O3 supports presigned URLs, allowing you to securely share access to buckets and objects for a limited time — without exposing credentials. This feature is fully compatible with AWS Signature Version 4 and works with `aws s3` commands while `aws s3api` does not have a corresponding command for generating presigned URLs. 

## What Is a Presigned URL?

A presigned URL is a time-limited, signed link that allows access to a specific object without requiring permanent credentials. Use it for:

- Secure file downloads
- Sharing files with third-party users or tools
- Temporary, credential-free uploads (not available using the AWS CLI, you must use an AWS SDK to create pre-signed URLs for upload)

## Generate a Presigned URL for Download
```bash
aws s3 presign s3://my-akave-bucket/myfile.txt \
  --expires-in 3600 \
  --endpoint-url https://o3-rc1.akave.xyz
```
> This generates a URL valid for 1 hour (3600 seconds) to download the file.

## Use a Presigned URL to Download

Anyone with the URL can download the file:
```bash
curl "https://o3-rc1.akave.xyz/my-akave-bucket/myfile.txt?...signature..."
```
Or open it directly in a browser.


## Security Notes

- Presigned URLs enforce the expiration time included in the signature.
  - The default expiration time is 1 hour (3600 seconds) when not using the optional `--expires-in` flag
  - Although the [presign function in AWS S3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html) has an expiration time limit of 1 week (604800 seconds) Akave O3 does not enforce this limitation, allowing for greater flexibility in temporary resource sharing
- Access control still applies; only users with appropriate credentials can generate URLs.
- If on-chain ACLs or permissions change before the URL is used, the request will be denied.
