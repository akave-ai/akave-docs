---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'CORS Examples'
weight: 11
cascade:
  type: docs
---

This page provides common CORS configuration examples for use with Akave O3. Save these as `cors.json` and use them with the `put-bucket-cors` command via `aws s3api`.

{{< callout type="info" >}}
**Important:** Replace `<YOUR_ENDPOINT_URL>` in these examples with your specific endpoint URL. Find your endpoint in the [Akave Environment](/akave-o3/introduction/akave-environment) page.
{{< /callout >}}

## Allow All Origins (Public Read)
```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET"],
      "AllowedOrigins": ["*"],
      "MaxAgeSeconds": 3000
    }
  ]
}
```
## Allow Specific Origin (e.g. frontend site)
```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["Authorization"],
      "AllowedMethods": ["GET", "PUT"],
      "AllowedOrigins": ["https://frontend.example.com"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 600
    }
  ]
}
```
## Allow Web Uploads from Browser
```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["POST", "PUT", "GET"],
      "AllowedOrigins": ["https://app.example.com"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```
## How to Use with CLI

Save any of these examples to a file named `cors.json`, then run:
```bash
aws s3api put-bucket-cors \
  --bucket my-akave-bucket \
  --cors-configuration file://cors.json \
  --endpoint-url <YOUR_ENDPOINT_URL>
```
This will apply the configuration to your bucket.