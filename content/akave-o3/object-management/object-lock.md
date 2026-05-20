---
date: '2026-02-23T20:26:00-00:00'
draft: false
title: 'Object Lock'
weight: 8
cascade:
  type: docs
---

Akave O3 supports S3-compatible Object Lock, enabling you to prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. This feature is essential for compliance requirements and data protection scenarios where write-once-read-many (WORM) capabilities are needed.

Object Lock can be enabled when creating the bucket or after one has been created, but the bucket **must be empty**. You cannot enable Object Lock on a non-empty bucket.

For more details on S3 Object Lock concepts, see the [AWS S3 Object Lock documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

{{< callout type="info" >}}
**Important:** Replace `<YOUR_ENDPOINT_URL>` in these examples with your specific endpoint URL. Find your endpoint in the [Akave Environment](/akave-o3/introduction/akave-environment) page.
{{< /callout >}}

<!-- Versioning should always be on -->
<!-- {{< callout type="warning" >}}
Object Lock requires versioning to be enabled on the bucket. Once Object Lock is enabled, it **cannot be disabled**, and versioning **cannot be suspended**.
{{< /callout >}} -->

### Create a Bucket with Object Lock

**Using `aws s3api`:**

```bash
aws s3api create-bucket \
  --bucket my-locked-bucket \
  --object-lock-enabled-for-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### Enable Object Lock on an Empty Bucket

**Using `aws s3api`:**
<!-- 
```bash
aws s3api put-bucket-versioning \
  --bucket my-akave-bucket \
  --versioning-configuration Status=Enabled \
  --endpoint-url <YOUR_ENDPOINT_URL>
``` -->

Enable Object Lock with a default retention rule:

```bash
aws s3api put-object-lock-configuration \
  --bucket my-akave-bucket \
  --object-lock-configuration '{
    "ObjectLockEnabled": "Enabled",
    "Rule": {
      "DefaultRetention": {
        "Mode": "GOVERNANCE",
        "Days": 30
      }
    }
  }' \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

To verify the configuration:

```bash
aws s3api get-object-lock-configuration \
  --bucket my-akave-bucket \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### Set and View Object Retention

**Using `aws s3api`:**

```bash
aws s3api put-object-retention \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --retention '{
    "Mode": "COMPLIANCE",
    "RetainUntilDate": "2026-12-31T00:00:00Z"
  }' \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

```bash
aws s3api get-object-retention \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

You can also set retention at upload time:

```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --body ./myfile.txt \
  --object-lock-mode GOVERNANCE \
  --object-lock-retain-until-date 2026-12-31T00:00:00Z \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### Manage Legal Hold

Legal Hold can be set independently of retention windows.

Enable Legal Hold:

```bash
aws s3api put-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --legal-hold Status=ON \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

Check Legal Hold status:

```bash
aws s3api get-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

Remove Legal Hold:

```bash
aws s3api put-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --legal-hold Status=OFF \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

### Retention Modes

| Action | GOVERNANCE | COMPLIANCE |
| --- | --- | --- |
| Delete locked version | Blocked | Blocked |
| Overwrite locked object | Blocked | Blocked |
| Shorten retention | Blocked | Blocked |
| Extend retention | Allowed | Allowed |

### Delete Behavior with Object Lock

- **Delete without `--version-id`** creates a delete marker and does not remove protected versions.
- **Delete with `--version-id`** attempts to permanently remove that version and is blocked while retention or Legal Hold is active.

```bash
aws s3api delete-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --version-id <version-id> \
  --endpoint-url <YOUR_ENDPOINT_URL>
```
