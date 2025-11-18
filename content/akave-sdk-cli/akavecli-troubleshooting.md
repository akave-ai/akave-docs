---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Troubleshooting the Akave CLI'
weight: 70
cascade:
  type: docs
---

This page lists known issues when using the Akave CLI and provides workarounds.

## 1. Versioned Files from O3 Create Directories on Download

### Symptom

When using a self-hosted **Akave O3** instance with **bucket versioning** enabled, object names on the Akave network can include version suffixes such as:

- `file.txt/null`
- `file.txt/V1`
- `file.txt/V2`

When downloading such a file with `akavecli`, you may see:

- A directory named `file.txt`
- A file inside that directory named `null`, `V1`, `V2`, etc.

Example:

```bash
cd file.txt
ls
V1
```

### Cause

The CLI interprets the `/` in the object name as a directory separator:

- `file.txt` becomes a directory
- The portion after `/` becomes the filename inside that directory

### Workaround

If you want to download and restore the file under its expected flat name (e.g., `file.txt`), follow these steps.

Assume:

- Bucket: `<bucket-name>`
- Object key: `file.txt/null`
- Desired final filename: `file.txt`

1. Create a directory with the file name:

```bash
mkdir file.txt
```

2. Download the file into that directory:

```bash
akavecli file download <bucket-name> file.txt/null . \
    --account <wallet-name> \
    --node-address connect.akave.ai:5500
```

After this, you will have:

- Directory: `file.txt`
- Inside it: file named `null` (or `V1`, etc.)

3. Change into the directory:

```bash
cd file.txt
```

4. Move the versioned file up one level and rename it temporarily:

```bash
mv * ../file.tmp
```

5. Go back and remove the now-empty directory:

```bash
cd ..
rmdir file.txt
```

6. Rename the temporary file to the original intended filename:

```bash
mv file.tmp file.txt
```

You will now have a flat file named `file.txt` in the current directory.

### Additional Troubleshooting

If you encounter other repeatable issues with `akavecli` consider:
- Running with additional logging or `--verbose` flags (where available)
- Verifying `--node-address` points to the correct network
- Confirming the wallet `--account` has sufficient balance and exists locally

You can also refer back to:

- [Bucket and File Commands]({{< relref "akave-sdk-cli/akavecli-bucket-file.md" >}}) for usage patterns
- [PDP Archival Usage]({{< relref "akave-sdk-cli/akavecli-pdp-archival.md" >}}) for archival-related behavior

If you have other questions, need technical guidance, or want to connect with other builders:

- **Email Our Support:** support@akave.io
- **Visit Our Support Page:** https://support.akave.xyz
- **Join Our Telegram Builders Group:** https://t.me/akavebuilders