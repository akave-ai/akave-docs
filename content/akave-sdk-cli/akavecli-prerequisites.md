---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Akave CLI Prerequisites'
weight: 20
cascade:
  type: docs
---

This page covers the prerequisites for using the **Akave CLI (`akavecli`)**.

## Go (for building from source)

If you are building the CLI from source, you need:

- **Go 1.23.5 or newer**

For the latest installation instructions, see:

`https://go.dev/doc/install`

### Example: macOS (Homebrew)

```bash
brew install go
brew upgrade go
go version
```

### Example: Ubuntu

```bash
wget https://go.dev/dl/go1.23.5.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
```
Add Go to your PATH in `~/.bashrc`:

```bash
export PATH=$PATH:/usr/local/go/bin
```

Reload your shell:

```bash
source ~/.bashrc
```

Verify:

```bash
go version
```

## Wallet

Akave CLI includes an integrated **wallet system**, so you do not need to manage raw private keys manually.

Wallets are stored locally at (by default): `~/.akave_wallets`

You can:

- Create a wallet
- Import an existing private key
- List wallets
- Export stored private keys

See: [Wallet Management]({{< relref "akave-sdk-cli/akavecli-wallet.md" >}})

## Node Address

To interact with the Akave network you need an RPC address.

- Public hosted network: `connect.akave.ai:5500`

- Archival Storage: `connect.akave.ai:9500`

All CLI commands accept: `--node-address=<host:port>`

## MetaMask and On-Chain Identity (Optional)

You can use MetaMask (or another EVM wallet) to manage your Akave address off-chain, and then:

- Export the private key from MetaMask
- Import it into `akavecli` using `wallet import`

For MetaMask export instructions: https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/
