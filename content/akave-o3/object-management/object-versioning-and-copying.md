---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Object Versioning and Copying'
weight: 7
cascade:
  type: docs
---

Akave O3 has S3-compatible object versioning and copying enabled by default, allowing you to preserve file history, retrieve older versions, and copy data within or across buckets -- all using familiar AWS CLI tools.

{{< callout type="info" >}}
Note that versioning **cannot be disabled** on Akave O3 as data is immutably stored on the blockchain.
{{< /callout >}}

### List Object Versions

**Using `aws s3api`:**

```bash
aws s3api list-object-versions \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 ls s3://my-akave-bucket --recursive --human-readable \
  --endpoint-url https://o3-rc2.akave.xyz
```

> Note: `aws s3` will show the latest versions only. Use `s3api` for full version metadata.


### Download a Specific Version

**Using `aws s3api`:**

```bash
aws s3api get-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --version-id <version-id> \
  ./myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**  
> Not directly supported for specific versions. Use `s3api` if version targeting is required.


### Delete a Specific Version

**Using `aws s3api`:**

```bash
aws s3api delete-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --version-id <version-id> \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**  
> Not supported — use `s3api` for versioned object deletion.


### Copy an Object

**Within the same bucket (using `s3api`):**

```bash
aws s3api copy-object \
  --bucket my-akave-bucket \
  --copy-source my-akave-bucket/myfile.txt \
  --key myfile-copy.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 cp s3://my-akave-bucket/myfile.txt s3://my-akave-bucket/myfile-copy.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Across buckets:**

```bash
aws s3 cp s3://source-bucket/myfile.txt s3://destination-bucket/myfile-copy.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

> **Note:** While `aws s3api` offers full control over versioning and metadata, `aws s3` is easier for basic operations. Use them together for a flexible Akave O3 workflow.