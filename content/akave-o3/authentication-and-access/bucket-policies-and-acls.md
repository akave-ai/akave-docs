---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Bucket Policies and ACLs'
weight: 23
cascade:
  type: docs
---

Access Control List (ACL) policies in Akave O3 allow your bucket to be accessed by users with the appropriate permissions, or allow your bucket to be accessed by anyone with public access.

Akave O3 supports full S3-compatible ACL configuration via the `aws s3api`.

## Put an ACL Policy

Start by creating a JSON file with the ACL policy you want to apply. For example, to allow public read access to your bucket, you can create a file called `acl.json` with the following content:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-akave-bucket/*"
        }
    ]
}
```

You can then apply the ACL policy to your bucket using the `aws s3api put-bucket-policy` command:
```bash
aws s3api put-bucket-policy \
  --bucket my-akave-bucket \
  --policy file://acl.json \
  --endpoint-url https://o3-rc1.akave.xyz
```

## Confirm the ACL Policy

You can confirm the ACL policy has been applied to your bucket using the `aws s3api get-bucket-policy` command:
```bash
aws s3api get-bucket-policy \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

Which will return the policy if it has been applied.

```json
{
    "Policy": "{\"policy\":{\"statement\":[{\"effect\":\"Allow\",\"principal\":\"*\",\"action\":\"s3:GetObject\",\"resource\":\"arn:aws:s3:::my-akave-bucket/*\"}},\"version\":\"2012-10-17\"}}"
}
```

Verify the policy has been applied by loading the data in a browser or with a CURL command with the following URL structure:
```
https://my-akave-bucket.o3-rc1.akave.xyz/your-object-name
```

If the policy has been applied, you should see the object data in the browser or in the response from the CURL command.

{{< callout type="info" >}}
**Note:** Most browsers will render the information in browser if it is an image file such as .png or .jpg, otherwise the browser will attempt to download the file.
{{< /callout >}}

## Delete the ACL Policy

You can delete the ACL policy from your bucket using the `aws s3api delete-bucket-policy` command:
```bash
aws s3api delete-bucket-policy \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

To verify the policy has been deleted, you can use the `aws s3api get-bucket-policy` command:
```bash
aws s3api get-bucket-policy \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc1.akave.xyz
```

Which will return an empty response if the policy has been deleted.

```json
{
    "Policy": "{\"policy\":{\"statement\":null,\"version\":\"\"}}"
}
```

If the policy has been deleted, you should also see an error message like the one below when attempting to access the object via the browser or CURL command:
```xml
<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
<Reason>Object ACL not found</Reason>
<Resource/>
<RequestId/>
<HostId/>
</Error>
```
