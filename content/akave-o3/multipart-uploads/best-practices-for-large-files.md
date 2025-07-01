---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Best Practices for Large Files'
weight: 9
cascade:
  type: docs
---

When working with large files on Akave O3 using multipart uploads, following best practices ensures optimal performance, data integrity, and efficient resource usage.

## Use Multipart Upload for Files > 1000 MB

While multipart upload technically kicks in around 8 MB (default in AWS CLI), Akave recommends explicitly using multipart upload for any file **over 1000 MB**, especially in decentralized environments where transfer stability and recovery are critical.

## Choose Optimal Part Size

- Minimum part size is **5 MB** (except the last part).
- For large files (e.g. 1–5 GB), use **50 MB to 100 MB** per part.
- For very large files (>5 GB), consider increasing part size to reduce number of API calls.

You can control this in `aws s3 cp` using:

--part-size 64MB

## Upload Parts in Parallel

Uploading parts in parallel improves speed significantly, especially over high-latency or geographically distributed connections.

- Use multi-threaded tools or scripts.
- Some SDKs and the `aws s3` high-level commands do this automatically.

## Capture ETags on Each Part Upload

When using `aws s3api upload-part`, always record the returned **ETag** value — it’s required to complete the multipart upload.

Store them in a temporary file or variable structure for use in `aws s3api complete-multipart-upload`.

## Abort Failed or Incomplete Uploads

Multipart uploads that aren’t completed **will persist** as orphaned parts, consuming storage.

Always:
- Use `aws s3api abort-multipart-upload` if your process fails or is interrupted.
- Periodically run `aws s3api list-multipart-uploads` to clean up stale uploads.

## Validate Upload Results

After completing a multipart upload:
- Use `aws s3api head-object` or `aws s3 ls` to confirm the file exists.
- Optionally download and checksum the file for data integrity validation.

## Use Streaming Upload for Large Data Pipelines

If you're building ingestion pipelines (e.g. video, AI/ML, log data):
- Consider streaming data directly into Akave O3 using multipart uploads or chunked transfers.
- Use the O3 API endpoint that is closest to your compute location for optimal performance.
