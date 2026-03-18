---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Create, List, Delete Buckets'
weight: 5
cascade:
  type: docs
---

Akave O3 is fully compatible with AWS CLI tooling. You can use both `aws s3api` and higher-level `aws s3` commands to interact with decentralized buckets and objects.

{{< callout type="info" >}}
**Important:** Replace `<YOUR_ENDPOINT_URL>` in these examples with your specific endpoint URL. Find your endpoint in the [Akave Environment](/akave-o3/introduction/akave-environment) page.
{{< /callout >}}

### Create a Bucket

**Using `aws s3api`:**

```bash
aws s3api create-bucket \
  --bucket my-akave-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

**Using `aws s3`:**

```bash
aws s3 mb s3://my-akave-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### List Buckets

**Using `aws s3api`:**

```bash
aws s3api list-buckets \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

**Using `aws s3`:**

```bash
aws s3 ls \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### Delete a Bucket

**Using `aws s3api`:**

```bash
aws s3api delete-bucket \
  --bucket my-akave-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

**Using `aws s3`:**

```bash
aws s3 rb s3://my-akave-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```


**Notes**: 
- Make sure your bucket is empty before deleting it. The operation will fail otherwise!
  - Akave has object versioning enabled by default, so to delete objects you must delete **each** object version. Specific instructions for deleting object versions can be found in the [Object Versioning and Copying](/akave-o3/object-management/object-versioning-and-copying/) section.
<!-- - After a bucket has been deleted a bucket cannot be created with the same name across the O3 instance, so be careful when deleting!  -->