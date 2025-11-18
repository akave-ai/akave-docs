---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'PDP Archival and Akave CLI'
weight: 60
cascade:
  type: docs
---

Akave integrates **Proof-of-Data-Possession (PDP)** for an archival storage tier backed by PDP-serving providers (PDP-SPs).

This section explains:

- How data flows into PDP archival storage
- How to check archival status
- How to download via PDP

{{< callout type="info" >}}
You must use node-address: `connect.akave.ai:9500` to access archival tier of Akave Storage. 
{{< /callout >}}

## 1. Uploading Data

Data upload with PDP does not require any special flags; archival happens in the background as part of the network’s pipeline.

Standard upload:

```bash
akavecli file upload <bucket> <file> \
  --account <wallet-name> \
  --node-address connect.akave.ai:9500
```
Once uploaded, the file is first available from the primary storage tier. Over time, it becomes available in archival PDP storage.

## 2. PDP Archival Cadence (1.6 GB Batches)

Archival uploads to PDP-SPs occur in **batches/ peices of approximately 1.6 GB** across the network.

This implies:

- Data is **not** immediately PDP-available after upload.
- The network aggregates data until it reaches a multiple of 1.6 GB:
  - If the network has uploaded `1.6 * n GB`, your data becomes PDP-available when the network reaches `1.6 * (n+1) GB`.
- PDP archival availability is therefore **eventually consistent**.
- Data once uploded to PDP archival layer is then deleted from Akave Storage Nodes.

If your file is not yet PDP-available, you can still download it using standard storage (without `--archival`).

## 3. Checking PDP Archival Status

Use the `archival-metadata` command:

```bash
akavecli archival-metadata <bucket> <file> \
  --account <wallet-name> \
  --node-address connect.akave.ai:9500
```

Example outputs:

- Fully available:

```bash
  Bucket: test1, File: test100mb.txt
  Status: Available for download from archival storage (all blocks have PDP data)
```

- Not fully available:

```bash
  Bucket: test1, File: test-5gb.txt
  Status: Not fully available in archival storage (some blocks are missing PDP data)
```

### Verbose Mode

Add `-v` or `--verbose` to include detailed chunk and block information:

```bash
akavecli archival-metadata <bucket> <file> \
  --account <wallet-name> \
  --node-address connect.akave.ai:5500 \
  --verbose
```
Verbose output includes:

- Total chunks
- Chunk CIDs
- Block CIDs
- PDP-SP URLs per block
- Offsets and sizes

This is useful for debugging archival gaps or looking up status of Dataset on [Filecoin's PDP Explorer](https://pdp.vxb.ai/mainnet/datasets).

## 4. Downloading Data via PDP

To explicitly download from PDP archival storage:

```bash
akavecli file download <bucket> <file> <output-dir> \
  --archival \
  --account <wallet-name> \
  --node-address connect.akave.ai:9500
```


