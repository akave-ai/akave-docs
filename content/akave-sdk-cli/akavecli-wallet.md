---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Wallet Management with Akave CLI'
weight: 40
cascade:
  type: docs
---

The Akave CLI includes a built-in **wallet subsystem** so you no longer need to pass raw private keys on every command.

From `akavecli --help`:

- Top-level command: `wallet`
- Global flags include:

    --account string          Optional: Wallet name to use. If not provided, will use the first available wallet
    --node-address string     The address of the node RPC (default "127.0.0.1:5000")
    --private-key string      Private key for signing transactions (advanced / optional)
    --metadata-encryption     Enable metadata encryption
    --encryption-key string   Encryption key for encrypting file data

## Wallet Storage

Wallets are stored in:

    ~/.akave_wallets

## Create a New Wallet

    akavecli wallet create

This will:

- Create a new wallet
- Store it in the keystore directory
- Assign it a wallet name

You can then use it via:

    --account <wallet-name>

If you do not pass `--account`, the CLI uses the **first available wallet**.

## List Wallets

    akavecli wallet list

This shows all wallets stored in the keystore.

## Import a Private Key

If you have a private key (e.g., exported from MetaMask), you can import it:

    akavecli wallet import <wallet-name> <private-key>

The CLI will create a wallet entry for that key, which you can then reference using `--account <wallet-name>`.

{{< callout type="warning" >}}
  Never share your private key with anyone.  
  Do not paste it into shared logs, screenshots, or public repositories.
{{< /callout >}}

## Export a Private Key

To export the private key for a wallet:

    akavecli wallet export-key <wallet-name>

Use this only when necessary (e.g., migrating to a different wallet system). Treat the exported key as extremely sensitive.

## Using Wallets in Commands

Every state-changing command that interacts with the network should be associated with a wallet.

Example:

    akavecli bucket create mybucket \
      --account mywallet \
      --node-address connect.akave.ai:5500

If `--account` is not provided, and at least one wallet exists, the first wallet in the keystore will be used.

## Advanced: Using --private-key Directly (Optional)

The recommended way is to use wallets. However, `--private-key` is still available for advanced flows or automated environments.

{{< callout type="info" >}}
If you must use `--private-key`, avoid typing the raw key in the command line directly. Use a file or environment variable where possible.
{{< /callout >}}

### Approach 1: Private Key File

1. Create a secure directory and file:

    mkdir -p ~/.key
    echo "your-private-key-content" > ~/.key/user.akvf.key
    chmod 600 ~/.key/user.akvf.key

2. Use it in commands:

    akavecli bucket create workshop \
      --private-key "$(cat ~/.key/user.akvf.key)" \
      --node-address connect.akave.ai:5500

### Approach 2: Environment Variable

1. Set the variable for the current session:

    export AKAVE_PRIVATE_KEY="<private-key>"

2. Use it in commands:

    akavecli bucket create workshop \
      --private-key "$AKAVE_PRIVATE_KEY" \
      --node-address connect.akave.ai:5500

3. Clear when done:

    unset AKAVE_PRIVATE_KEY

If you add the `export` line to your shell RC (`~/.bashrc` or `~/.zshrc`), it will be available in every new shell session. Be sure your machine is secure and not shared if you choose this approach.
