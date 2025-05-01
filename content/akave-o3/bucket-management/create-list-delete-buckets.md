---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Create, List, Delete Buckets'
weight: 5
cascade:
  type: docs
---

Akave O3 is fully compatible with AWS CLI tooling. You can use both `aws s3api` and higher-level `aws s3` commands to interact with decentralized buckets and objects - all through for exmaple the IPC API `https://o3-rc1.akave.xyz` endpoint.

### Create a Bucket

**Using `aws s3api`:**

```bash
aws s3api create-bucket \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 mb s3://my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

### List Buckets

**Using `aws s3api`:**

```bash
aws s3api list-buckets \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 ls \
  --endpoint-url https://o3-rc1.akave.xyz
```

### Delete a Bucket

**Using `aws s3api`:**

```bash
aws s3api delete-bucket \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 rb s3://my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Note**: Make sure your bucket is empty before deleting it. The operation will fail otherwise!