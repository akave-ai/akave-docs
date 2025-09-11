---
date: '2025-04-28T21:41:52-05:00'
draft: true
title: 'Server-side and Client-side Encryption'
weight: 14
cascade:
  type: docs
---

Akave O3 supports both **Server-Side Encryption (SSE)** and **Client-Side Encryption (CSE)** through the S3-compatible API. You can enforce encryption policies at the bucket level or specify encryption settings at upload time.

## Server-Side Encryption (SSE)

With SSE, Akave encrypts your objects at rest using one of the supported methods:

- `AES256` (SSE-S3 compatible)
- `aws:kms` (reserved for future integration with Akave Key Management)

### Enable SSE by Default (Bucket Level)

**Using `aws s3api`:**
```bash
aws s3api put-bucket-encryption \
  --bucket my-akave-bucket \
  --server-side-encryption-configuration file://sse.json \
  --endpoint-url https://o3-rc2.akave.xyz
```
**Example `sse.json`:**
```json
{
  "Rules": [
    {
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }
  ]
}
```
### View Bucket Encryption Setting

**Using `aws s3api`:**
```bash
aws s3api get-bucket-encryption \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```
## Disable Bucket Encryption

**Using `aws s3api`:**
```bash
aws s3api delete-bucket-encryption \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```
**Note:** The bucket must be empty for bucket encryption to be removed. See the [Delete an Object](https://docs.akave.xyz/akave-o3/object-management/upload-download-delete-objects/#delete-an-object) section for how to remove objects from a bucket.

## Client-Side Encryption (CSE)

Client-side encryption is handled **before** data reaches the Akave network. You are responsible for managing encryption keys and performing encryption/decryption locally.

### Upload with Custom Client-Side Encryption

**Using `aws s3`:**
```bash
aws s3 cp myfile.txt s3://my-akave-bucket/encrypted.txt \
  --sse AES256 \
  --endpoint-url https://o3-rc2.akave.xyz
```
**Using `aws s3api`:**
```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key encrypted.txt \
  --body myfile.txt \
  --server-side-encryption AES256 \
  --endpoint-url https://o3-rc2.akave.xyz
```
{{< callout type="info" >}}
 - SSE is best for simplifying key handling while maintaining secure storage at rest.
 - CSE offers full control and is ideal for sensitive data but requires careful key management.
 - Akave does not store or manage your encryption keys unless you explicitly use Akave.Cloud key features.
{{< /callout >}}
