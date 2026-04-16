---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Bucket and File Commands'
weight: 50
cascade:
  type: docs
schema_json: |
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "Create Buckets and Upload Files with Akave",
    "description": "Create, list, and delete storage buckets, and upload, download, and manage files in Akave sovereign cloud storage.",
    "step": [
      { "@type": "HowToStep", "text": "Follow the instructions on this page." }
    ]
  }
---

This page documents the main **bucket** and **file** commands in `akavecli`.

Global flags you will commonly use:

- `--account <wallet-name>` which wallet to use
- `--node-address <host:port>` Akave node RPC address
- `--metadata-encryption` enable metadata encryption
- `--encryption-key "<key>"` encryption key for file data

## Buckets

### Create Bucket

Creates a new bucket on the Akave network.

```bash
akavecli bucket create <bucket-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### Delete Bucket

Soft deletes a bucket.

```bash
akavecli bucket delete <bucket-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### View Bucket

Shows details for a specific bucket.

```bash
akavecli bucket view <bucket-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### List Buckets

Lists all buckets associated with the selected account.

```bash
akavecli bucket list \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

## Files

{{< callout type="info" >}}
The maximum file size for a single `akavecli` upload is **5 GB**. For larger objects, use **Multipart Uploads** with the [Akave O3 API](/akave-o3/multipart-uploads/best-practices-for-large-files/).
{{< /callout >}}

### List Files in a Bucket

List all the files in specified bucket 

```bash
akavecli file list <bucket-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### Get File Info

Fetches metadata about a file.

```bash
akavecli file info <bucket-name> <file-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### Upload File

Uploads a file from your local filesystem into the bucket.

```bash
akavecli file upload <bucket-name> <file-path> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

You may also add:

- `--metadata-encryption`
- `--encryption-key "<key>"`

for encrypted data and metadata.

### Download File

Downloads a file from a bucket.

```bash
akavecli file download <bucket-name> <file-name> <destination-folder> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```

### Delete File

Removes a file from a bucket.

```bash
akavecli file delete <bucket-name> <file-name> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500
```