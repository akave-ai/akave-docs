---
date: '2026-02-23T20:26:00-00:00'
draft: true
title: 'Object Lock'
weight: 8
cascade:
  type: docs
---

Akave O3 supports S3-compatible Object Lock, enabling you to prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. This feature is essential for compliance requirements and data protection scenarios where write-once-read-many (WORM) capabilities are needed.

<!-- Versioning should always be on -->
<!-- {{< callout type="warning" >}}
Object Lock requires versioning to be enabled on the bucket. Once Object Lock is enabled, it **cannot be disabled**, and versioning **cannot be suspended**.
{{< /callout >}} -->

### Enable Object Lock on a Bucket

**Using `aws s3api`:**
<!-- 
```bash
aws s3api put-bucket-versioning \
  --bucket my-akave-bucket \
  --versioning-configuration Status=Enabled \
  --endpoint-url https://o3-rc2.akave.xyz
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
  --endpoint-url https://o3-rc2.akave.xyz
```

To verify the configuration:

```bash
aws s3api get-object-lock-configuration \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
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
  --endpoint-url https://o3-rc2.akave.xyz
```

```bash
aws s3api get-object-retention \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

You can also set retention at upload time:

```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --body ./myfile.txt \
  --object-lock-mode GOVERNANCE \
  --object-lock-retain-until-date 2026-12-31T00:00:00Z \
  --endpoint-url https://o3-rc2.akave.xyz
```

### Manage Legal Hold

Legal Hold can be set independently of retention windows.

Enable Legal Hold:

```bash
aws s3api put-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --legal-hold Status=ON \
  --endpoint-url https://o3-rc2.akave.xyz
```

Check Legal Hold status:

```bash
aws s3api get-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

Remove Legal Hold:

```bash
aws s3api put-object-legal-hold \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --legal-hold Status=OFF \
  --endpoint-url https://o3-rc2.akave.xyz
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
  --endpoint-url https://o3-rc2.akave.xyz
```

{{< callout type="info" >}}
For more details on S3 Object Lock concepts, see the [AWS S3 Object Lock documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
{{< /callout >}}
