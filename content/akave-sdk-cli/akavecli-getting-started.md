---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Getting Started'
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

[https://explorer.akave.ai](https://explorer.akave.ai)

Use the Akave blockchain explorer to inspect blocks, transactions, and storage-related activity on the Akave chain.

### Faucet and Chain Setup

[https://faucet.akave.ai](https://faucet.akave.ai)

Visit the Akave Faucet to:

- Add the Akave chain to MetaMask using the **"Add Akave to Metamask"** button or by copying the RPC information and adding it manually
- Request test funds by pasting in your wallet address and clicking **"Claim AKVT"**

**Note:** If you don't yet have the MetaMask browser extension, visit [https://metamask.io](https://metamask.io) to download and install it. You can also create a wallet for use with the Akave CLI by using the [wallet management commands](/akave-sdk-cli/akavecli-wallet/).

![Akave Faucet](/images/faucet.gif)

### Public Node Address

The public endpoint for the Akave network is:

`--node-address=connect.akave.ai:5500`


## Where to Go Next

- [Prerequisites]({{< relref "akave-sdk-cli/akavecli-prerequisites.md" >}})
- [Install and Build the Akave CLI]({{< relref "akave-sdk-cli/akavecli-installation-build.md" >}})
- [Wallet Management]({{< relref "akave-sdk-cli/akavecli-wallet.md" >}})
- [Bucket and File Commands]({{< relref "akave-sdk-cli/akavecli-bucket-file.md" >}})
- [PDP Archival Usage]({{< relref "akave-sdk-cli/akavecli-pdp-archival.md" >}})
- [Troubleshooting the Akave CLI]({{< relref "akave-sdk-cli/akavecli-troubleshooting.md" >}})