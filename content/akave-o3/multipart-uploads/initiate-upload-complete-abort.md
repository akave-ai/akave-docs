---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Initiate, Complete, Abort Upload'
weight: 8
cascade:
  type: docs
---

Akave O3 supports `multipart uploads` for large files using the standard AWS S3-compatible API. This allows you to upload parts of a file independently, improving performance and fault tolerance.

Below are examples using both `aws s3api` and `aws s3` commands for initiating, completing, and aborting multipart uploads.

# Using `aws s3` (simple option)

The high-level `aws s3 cp` command will **automatically handle multipart uploads** when the file is large enough (default is 8 MB+):
```bash
aws s3 cp ./largefile.zip s3://my-akave-bucket/largefile.zip \
  --endpoint-url https://o3-rc1.akave.xyz
```
No need to manage `UploadId`, parts, or ETags manually.

> Use `--expected-size` and `--part-size` for more control during automatic multipart uploads.

# Using `aws s3api` (more granular)

## Initiate Multipart Upload

**Using `aws s3api`:**
```bash
aws s3api create-multipart-upload \
  --bucket my-akave-bucket \
  --key largefile.zip \
  --endpoint-url https://o3-rc1.akave.xyz
```
This returns an `UploadId` which you must reference in the next steps.


## Upload Parts

**Using `aws s3api`:**
```bash
aws s3api upload-part \
  --bucket my-akave-bucket \
  --key largefile.zip \
  --part-number 1 \
  --body part1.zip \
  --upload-id <UploadId> \
  --endpoint-url https://o3-rc1.akave.xyz
```
Repeat this step for each part of the file, incrementing the `--part-number`.


## Complete Multipart Upload

After uploading all parts, you must complete the upload with an XML or JSON structure describing the uploaded parts.

**Using `aws s3api`:**
```bash
aws s3api complete-multipart-upload \
  --bucket my-akave-bucket \
  --key largefile.zip \
  --upload-id <UploadId> \
  --multipart-upload file://parts.json \
  --endpoint-url https://o3-rc1.akave.xyz
```
`parts.json` should look like this:
```json
{
  "Parts": [
    {
      "ETag": "\"etag-part1\"",
      "PartNumber": 1
    },
    {
      "ETag": "\"etag-part2\"",
      "PartNumber": 2
    }
  ]
}
```
You can get ETags from the response of each `upload-part` command.


## Abort Multipart Upload

**Using `aws s3api`:**
```bash
aws s3api abort-multipart-upload \
  --bucket my-akave-bucket \
  --key largefile.zip \
  --upload-id <UploadId> \
  --endpoint-url https://o3-rc1.akave.xyz
```
This will cancel the upload and remove all uploaded parts.

{{< callout type="info" >}}
 Akave O3 supports multipart uploads via S3-compatible APIs only. IPC CLI support is not available for multipart uploads at this time.
{{< /callout >}}
