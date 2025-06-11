---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Debugging S3 Requests'
weight: 20
cascade:
  type: docs
---

When things go wrong with `aws s3` or `aws s3api` calls against Akave O3, the first step is to enable debug logging.

## Enable Debug Output

Add `--debug` to any AWS CLI command to see:

- HTTP request headers
- HTTP response codes
- Signature payloads
- Region and profile resolution

Example:
```bash
aws s3api list-buckets \
  --endpoint-url https://o3-rc1.akave.xyz \
  --debug
```
## Review Signature and Region

Check that:

- The region is set to `akave-network`
- You're using the correct profile (`--profile akave-o3`)
- Your credentials are loaded correctly

## Common Debug Traps

- SignatureDoesNotMatch → Incorrect region, invalid date, or credentials
- InvalidArgument → Unsupported header or parameter
- MissingContentMD5 → Some `put-object` operations now require content MD5 (especially with newer CLI versions)
- TLS errors → Confirm that the endpoint is HTTPS and correctly resolves

## Validate the Config File

Check `~/.aws/config` for:
```bash
[profile o3]  
region = akave-network  
request_checksum_calculation = WHEN_REQUIRED  
response_checksum_validation = WHEN_REQUIRED
```
## Advanced: Use curl for low-level testing

You can replicate basic S3 GET/PUT operations manually using presigned URLs or raw signature V4 requests if needed; useful to isolate SDK/CLI bugs.

## Stay Current

The AWS CLI and SDKs change frequently. If a bug is suspected:

- Check known issues on GitHub ([boto3](https://github.com/boto/boto3), [aws-cli](https://github.com/aws/aws-cli), [s3transfer](https://github.com/boto/s3transfer))
- Try downgrading or upgrading versions
- Use profiles with custom settings to isolate test cases
