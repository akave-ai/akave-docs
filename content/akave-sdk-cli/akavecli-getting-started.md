---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Blockchain Integrated Storage with Akave CLI'
weight: 11
cascade:
  type: docs
---

The **Akave CLI (`akavecli`)** is the primary tool for interacting with Akave’s decentralized storage network.

It enables:

- Creation and management of **buckets**
- Uploading/downloading **files**
- Managing **wallets and accounts**
- Interacting with Akave’s **blockchain-integrated storage**

Akave operates a blockchain-integrated storage layer where all storage actions are verifiable and tied to on-chain events.

## Explorer, Faucet, and Public Endpoint

### Blockchain Explorer

    http://explorer.akave.ai

Use this to inspect blocks, transactions, and storage-related activity on the Akave chain.

### Faucet and Chain Setup

To get started with a wallet and funds, visit:

    https://faucet.akave.ai

From there you can:

- Add the Akave chain to MetaMask / get RPC information
- Request test funds

![Akave Faucet](/images/faucet.gif)

### Public Node Address

The public endpoint for the Akave network is:

    --node-address=connect.akave.ai:5500


## Where to Go Next

- Prerequisites: {{< relref "akavecli-prerequisites.md" >}}
- Installation & Build: {{< relref "akavecli-installation-build.md" >}}
- Wallet Management: {{< relref "akavecli-wallet.md" >}}
- Bucket & File Commands: {{< relref "akavecli-bucket-file.md" >}}
- PDP Archival Usage: {{< relref "akavecli-pdp-archival.md" >}}
- Troubleshooting: {{< relref "akavecli-troubleshooting.md" >}}