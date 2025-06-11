---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Setting CORS Policies'
weight: 10
cascade:
  type: docs
---

Cross-Origin Resource Sharing (CORS) policies in Akave O3 allow your bucket to be accessed by web apps from other origins. This is essential for use cases involving frontend apps, embedded content, or external data consumers.

Akave O3 supports full S3-compatible CORS configuration via the `aws s3api`.

## Put a CORS Policy

**Using `aws s3api`:**
```bash
aws s3api put-bucket-cors \
  --bucket my-akave-bucket \
  --cors-configuration file://cors.json \
  --endpoint-url https://o3-rc1.akave.xyz
```
**Using `aws s3`:**

Not supported for CORS. Use `s3api` for CORS operations.

## View Current CORS Policy

**Using `aws s3api`:**
```bash
aws s3api get-bucket-cors \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```
## Delete Existing CORS Policy

**Using `aws s3api`:**
```bash
aws s3api delete-bucket-cors \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```
{{< callout type="info" >}}
 - CORS applies at the **bucket level**.
 - The configuration must be passed as a JSON file.
 - Improper CORS configuration may block access to your objects from browsers.
{{< /callout >}}

To create a valid configuration file, see the next section on CORS examples.
