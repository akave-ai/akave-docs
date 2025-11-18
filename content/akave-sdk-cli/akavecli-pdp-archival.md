---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'PDP Archival Usage'
weight: 60
cascade:
  type: docs
---

Akave integrates **Proof-of-Data-Possession (PDP)** for an archival storage tier backed by PDP-serving providers (PDP-SPs).

This section explains:

- How data flows into PDP archival storage
- How to check the archival status of a file
- How to download a file from archival storage using PDP

## About Filecoin's PDP Implementation

Akave's archival storage tier is powered by **Filecoin's Proof-of-Data-Possession (PDP)** protocol. PDP is a cryptographic proof system that allows storage providers to demonstrate they are storing client data without requiring the client to download the entire dataset for verification. Filecoin's PDP implementation enables:

- **Efficient verification**: Storage providers can prove data possession with minimal bandwidth
- **Decentralized archival**: Data is stored across multiple independent storage providers
- **Cost-effective long-term storage**: Leverages Filecoin's competitive storage marketplace

For new users looking to learn more about Filecoin's PDP implementation, visit the [Filecoin PDP documentation](https://docs.filecoin.cloud/core-concepts/pdp-overview/) and explore datasets on the [Filecoin PDP Explorer](https://pdp.vxb.ai/mainnet/datasets).

{{< callout type="info" >}}
You must use the node-address: `connect.akave.ai:9500` to access archival tier of Akave Storage. 
{{< /callout >}}

## 1. Uploading Data

Data upload with PDP does not require any special flags; archival processing happens in the background as part of the network’s pipeline.

Standard upload:

```bash
akavecli file upload <bucket> <file> \
  --account <wallet-name> \
  --node-address connect.akave.ai:9500
```
Once uploaded, the file is first available from the primary storage tier. After the network has aggregated the data into a multiple of 2 GB and uploaded it to PDP-SPs, it becomes available in archival PDP storage.

## 2. PDP Archival Cadence (2 GB Batches)

Archival uploads to PDP-SPs occur in **batches/ pieces of approximately 2 GB** across the network.

This implies:

- Data is **not** immediately PDP-available after upload.
- The network aggregates data until it reaches a multiple of 2 GB:
  - If the network has uploaded `2 * n GB`, your data becomes PDP-available when the network reaches `2 * (n+1) GB`.
- PDP archival availability is therefore **eventually consistent**.
- Data once it is uploaded to the PDP archival layer is then deleted from Akave Storage Nodes.

If your file is not yet PDP-available, you can still download it using standard storage (without the `--archival` flag).

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

To explicitly download from PDP archival storage, use the `--archival` flag:

```bash
akavecli file download <bucket> <file> <output-dir> \
  --archival \
  --account <wallet-name> \
  --node-address connect.akave.ai:9500
```


