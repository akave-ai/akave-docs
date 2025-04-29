---
date: '2025-04-29T12:15:00-05:00'
draft: false
title: '🌐 S3 Compatibility Overview'
weight: 3
cascade:
  type: docs
---

Akave O3 delivers seamless AWS S3 API compatibility to help developers and enterprises migrate cloud-native apps to decentralized infrastructure without code changes. Below is the full list of tested and supported operations as of release **v0.2.1**, with links to official AWS documentation for reference.

---

## ✅ Compatibility

Akave O3 is fully compatible with:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/s3/) (s3api, s3)
- [AWS SDK for PHP](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-examples.html)
- [AWS SDK for Go](https://docs.aws.amazon.com/sdk-for-go/api/service/s3/)
- [AWS SDK for Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html)

---

## ✅ Supported Features and Operations

### 🚀 Transfer Operations
- [aws s3 cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) – Copy files between local filesystem and bucket.
- [aws s3 mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) – Move files between local and bucket.

### 🪣 Bucket Operations
- [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) – Create a new S3 bucket.
- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) – Permanently delete an empty bucket.
- [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) – Check if a bucket exists and is accessible.
- [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) – Enable or suspend versioning on a bucket.

### 📦 Object Operations
- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) – Upload an object to a bucket.
- [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) – Download an object from a bucket.
- [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) – Retrieve metadata about an object.
- [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) – Delete a single object from a bucket.
- [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) – Delete multiple objects in a single request.

### 🏷️ Tagging Support
- [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) – Retrieve all tags assigned to an object.
- [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) – Add or update tags on an object.
- [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) – Remove all tags from an object.

### 🌐 CORS Support
- [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html) – Retrieve the CORS configuration of a bucket.
- [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html) – Set or update CORS configuration for a bucket.
- [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html) – Remove CORS rules from a bucket.

### 🔒 Encryption Support
- [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) – Get the encryption configuration of a bucket.
- [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) – Enable default encryption on a bucket.

### 📜 Policy and ACL Management
- [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html) – Attach a policy to a bucket.
- [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) – Retrieve the policy associated with a bucket.
- [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html) – Delete the policy attached to a bucket.
- [PutBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) – Set access permissions for a bucket.
- [GetBucketAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html) – Retrieve access control settings of a bucket.

---

## 🔗 External Resources
- [AWS CLI Reference for S3](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [AWS S3 API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)
- [AWS Signature Version 4 Signing Process](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)

---