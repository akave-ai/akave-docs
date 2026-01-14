---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Create, List, Delete Buckets'
weight: 5
cascade:
  type: docs
---

Akave O3 is fully compatible with AWS CLI tooling. You can use both `aws s3api` and higher-level `aws s3` commands to interact with decentralized buckets and objects - all through, for example, the `https://o3-rc2.akave.xyz` endpoint.

### Create a Bucket

**Using `aws s3api`:**

```bash
aws s3api create-bucket \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 mb s3://my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

### List Buckets

**Using `aws s3api`:**

```bash
aws s3api list-buckets \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 ls \
  --endpoint-url https://o3-rc2.akave.xyz
```

### Delete a Bucket

**Using `aws s3api`:**

```bash
aws s3api delete-bucket \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 rb s3://my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```


**Notes**: 
- Make sure your bucket is empty before deleting it. The operation will fail otherwise!
  - Akave has object versioning enabled by default, so to delete objects you must delete **each** object version. Specific instructions for deleting object versions can be found in the [Object Versioning and Copying](/akave-o3/object-management/object-versioning-and-copying/) section.
<!-- - After a bucket has been deleted a bucket cannot be created with the same name across the O3 instance, so be careful when deleting!  -->