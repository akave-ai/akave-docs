---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Upload, Download, Delete Objects'
weight: 6
cascade:
  type: docs
---



Once you've created a bucket in Akave O3, you can use standard AWS CLI commands to manage your objects. Below are examples using both `aws s3api` and the simpler `aws s3 cli` syntax.


### Upload an Object

**Using `aws s3api`:**

```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --body ./myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 cp ./myfile.txt s3://my-akave-bucket/myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```

### Download an Object

**Using `aws s3api`:**

```bash
aws s3api get-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  ./downloaded-myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 cp s3://my-akave-bucket/myfile.txt ./downloaded-myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```

### Delete an Object

**Using `aws s3api`:**

```bash
aws s3api delete-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 rm s3://my-akave-bucket/myfile.txt \
  --endpoint-url https://o3-rc1.akave.xyz
```
