---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Upload, Download, Delete Objects'
weight: 6
cascade:
  type: docs
---



Once you've created a bucket in Akave O3, you can use standard AWS CLI commands to manage your objects. Below are examples using both `aws s3api` and the simpler `aws s3` CLI syntax.


### Upload an Object

**Using `aws s3api`:**

```bash
aws s3api put-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --body ./myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 cp ./myfile.txt s3://my-akave-bucket/myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

### Download an Object

**Using `aws s3api`:**

```bash
aws s3api get-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  ./downloaded-myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 cp s3://my-akave-bucket/myfile.txt ./downloaded-myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

### List Objects

**Using `aws s3api`:**

```bash
aws s3api list-objects \
  --bucket my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 ls s3://my-akave-bucket \
  --endpoint-url https://o3-rc2.akave.xyz
```

### Total Size for All Objects in a Bucket

**Using `aws s3`:**

```bash
aws s3 ls s3://my-akave-bucket \
--recursive --human-readable --summarize \
--endpoint-url https://o3-rc2.akave.xyz
```

### Delete an Object

**Using `aws s3api`:**

```bash
aws s3api delete-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

**Using `aws s3`:**

```bash
aws s3 rm s3://my-akave-bucket/myfile.txt \
  --endpoint-url https://o3-rc2.akave.xyz
```

{{< callout type="info" >}}
 Akave O3 supports safe characters for object naming only. If using characters that require special handling please be aware that these are not fully supported and may cause issues with the O3 API. See [Naming Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html) for more information.
{{< /callout >}}

### View an Object's Root eCID

Objects uploaded using Akave O3 end up on the Akave network shortly after being uploaded depending on network activity. To see an object's encrypted content identifier ([eCID](https://akave.com/blog/rethinking-content-addressing-for-the-enterprise-introducing-ecid-by-akave)) you can use the `head object` command with the `aws s3api`:

```bash
aws s3api head-object \
  --bucket my-akave-bucket \
  --key myfile.txt \
  --endpoint-url=https://o3-rc2.akave.xyz
```

The eCID is then returned in the `Metadata` section of the response as `Network-Root-Cid`:

```json
{
    "LastModified": "2024-05-15T00:00:00+00:00",
    "ContentLength": 2194339,
    "ChecksumType": "FULL_OBJECT",
    "ETag": "\"/AUFzg+DN6yA3d95WCR31g==\"",
    "MissingMeta": 0,
    "VersionId": "V1",
    "ContentType": "image/png",
    "ServerSideEncryption": "AES256",
    "Metadata": {
        "Network-File-Name": "4c8da9604c2cea1085d41b446e07c335deae60636feaf4d0fcf6d67cbadabd013ae209ab478f0cde06c7cb03fe",
        "Network-Processed": "100",
        "Network-Root-Cid": "bafybeicun4bwqcby46mcxicctyob6vjd4lid74k3c4lzfaifl56sghrt3q",
        "Network-State": "done"
    },
    "StorageClass": "default",
    "PartsCount": 0
}
```