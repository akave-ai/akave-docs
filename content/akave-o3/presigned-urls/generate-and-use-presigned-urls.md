---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Generate and Use Presigned URLs'
weight: 9
cascade:
  type: docs
---

Akave O3 supports presigned URLs, allowing you to securely share access to buckets and objects for a limited time — without exposing credentials. This feature is fully compatible with AWS Signature Version 4 and works with both `aws s3` and `aws s3api`.

## What Is a Presigned URL?

A presigned URL is a time-limited, signed link that allows access to a specific object without requiring permanent credentials. Use it for:

- Secure file downloads
- Temporary, credential-free uploads
- Sharing files with third-party users or tools

## Generate a Presigned URL for Download

**Using `aws s3`:**
```bash
aws s3 presign s3://my-akave-bucket/myfile.txt \
  --expires-in 3600 \
  --endpoint-url https://o3-rc1.akave.xyz
```
**Using `aws s3api`:**
```bash
aws s3api generate-presigned-url \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --expires-in 3600 \
  --endpoint-url https://o3-rc1.akave.xyz
```
> This generates a URL valid for 1 hour (3600 seconds) to download the file.

## Generate a Presigned URL for Upload

**Using `aws s3`:**
```bash
aws s3 presign s3://my-akave-bucket/newfile.txt \
  --expires-in 600 \
  --http-method PUT \
  --endpoint-url https://o3-rc1.akave.xyz
```
**Using `aws s3api`:**
```bash
aws s3api generate-presigned-url \
  --bucket my-akave-bucket \
  --key newfile.txt \
  --expires-in 600 \
  --http-method PUT \
  --endpoint-url https://o3-rc1.akave.xyz
```
> This presigned URL allows a third party to upload a file using HTTP PUT.

## Use a Presigned URL to Download

Anyone with the URL can download the file:
```bash
curl "https://o3-rc1.akave.xyz/my-akave-bucket/myfile.txt?...signature..."
```
Or open it directly in a browser.

## Use a Presigned URL to Upload
```bash
curl -X PUT \
  --upload-file ./localfile.txt \
  "https://o3-rc1.akave.xyz/my-akave-bucket/newfile.txt?...signature..."
```

## Security Notes

- Presigned URLs enforce the expiration time included in the signature.
- Access control still applies; only users with appropriate credentials can generate URLs.
- If on-chain ACLs or permissions change before the URL is used, the request will be denied.