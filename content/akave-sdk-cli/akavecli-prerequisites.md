---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Prerequisites'
weight: 20
cascade:
  type: docs
---

This page covers the prerequisites for using the **Akave CLI (`akavecli`)** including:

- The Go Programming Language
- An Ethereum Compatible Wallet
- A Valid Akave Node Address
- MetaMask and On-Chain Identity (Optional)

## Go Programming Language

If you are building the Akave CLI from source, you need **Go version 1.23.5 or newer**.

For the latest installation instructions, see: [https://go.dev/doc/install](https://go.dev/doc/install)

### Installation Example: macOS (Homebrew)

To install Go on macOS using Homebrew, run:

```bash
brew install go
brew upgrade go
go version
```
If Go was installed successfully, you should see the version number in the output (e.g., `go version go1.23.5 darwin/amd64`).

### Installation Example: Ubuntu

To install Go on Ubuntu, run:

```bash
wget https://go.dev/dl/go1.23.5.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
```
Then, add Go to your PATH in `~/.bashrc`:

```bash
export PATH=$PATH:/usr/local/go/bin
```

Next, reload your shell:

```bash
source ~/.bashrc
```

Finally, verify that Go was installed successfully by running:

```bash
go version
```
If Go was installed successfully, you should see the version number in the output (e.g., `go version go1.23.5 linux/amd64`).

## Wallet

Akave's network runs on an EVM blockchain, so you need an Ethereum compatible wallet to manage your Akave address.

To make this process easier, the Akave CLI includes an integrated **wallet system**, so you do not need to manage raw private keys manually.

Wallets you've created or imported are stored locally on your machine at: `~/.akave_wallets`

The Akave CLI wallet system allows you to:

- Create a wallet
- Import an existing private key
- List wallets
- Export stored private keys

For more information, see: [Wallet Management]({{< relref "akave-sdk-cli/akavecli-wallet.md" >}})

## Node Address

To interact with the Akave network you need to use the `--node-address` flag with an RPC address.

- Akave Hot Storage: `connect.akave.ai:5500`

- Akave Archival Storage with Filecoin: `connect.akave.ai:9500`

All Akave CLI commands accept the `--node-address` flag: `--node-address=<host:port>`

## MetaMask and On-Chain Identity (Optional)

You can use MetaMask (or another EVM wallet) to manage your Akave address by:

- Exporting a private key from MetaMask
- Importing it into the Akave CLI using the `akavecli wallet import` command

For instructions on how to export a private key from MetaMask, see: https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/


## Next Steps

Now that you have completed the prerequisites, you can proceed to [Install and Build Akave CLI]({{< relref "akave-sdk-cli/akavecli-installation-build.md" >}}).
