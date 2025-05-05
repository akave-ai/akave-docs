---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Upload, Download, Delete Objects'
weight: 6
cascade:
  type: docs
---

## Uploading, Downloading, and Deleting Objects with AWS CLI

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

### List Objects

**Using `aws s3api`:**

```bash
aws s3api list-objects \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

**Note:** When using the "list-objects" command with the aws s3api you may notice that your objects have /null following their key. This is expected behavior and represents that you are not using object versioning, so the object you've uploaded has no version associated with it.
```bash
"Key": "myfile.txt/null",
```

**Using `aws s3`:**

```bash
aws s3 ls s3://my-akave-bucket \
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
