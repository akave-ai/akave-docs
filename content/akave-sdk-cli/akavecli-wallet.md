---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Wallet Management'
weight: 40
cascade:
  type: docs
---

The Akave CLI includes a built-in **wallet subsystem** to prevent needing to pass raw private keys with every command, minimizing the risk of exposure.

Run `akavecli wallet --help` to see available wallet commands:

- `balance`     Shows the AKVT token balance for a wallet
- `create`      Creates a new wallet
- `export-key`  Exports private key for a wallet
- `import`      Import a wallet using a private key
- `list`        Lists all wallets

## Wallet Storage

Wallets are stored in: `~/.akave_wallets`

## Usage Examples

### Create a New Wallet

```bash
akavecli wallet create
```
This will:

- Create a new wallet
- Store it in the keystore directory
- Assign it a wallet name

You can then use it with [bucket and file commands](/akave-sdk-cli/akavecli-bucket-file) via the `--account` flag:

```bash
akavecli bucket create mybucket --account <wallet-name>
```

**Note:** If you do not use the `--account` flag, the CLI uses the **first available wallet**.

### List Wallets

```bash
akavecli wallet list
```

This shows all wallets stored in the keystore.

### Import a Private Key

If you have a private key (e.g., exported from MetaMask), you can import it using:

```bash
akavecli wallet import <wallet-name> <private-key>
```

The CLI will create a wallet entry for that key, which you can then reference using `--account <wallet-name>`.

{{< callout type="warning" >}}
  Never share your private key with anyone. Do not paste it into shared logs, screenshots, or public repositories.
{{< /callout >}}

### Export a Private Key

To export the private key for a wallet, use:

```bash
akavecli wallet export-key <wallet-name>
```

Use this only when necessary (e.g., migrating to a different wallet system). Treat the exported key as extremely sensitive.

## Using Wallets in Commands

Every state-changing command that interacts with the network should be associated with a wallet.

Example:

```bash
akavecli bucket create mybucket \
      --account mywallet \
      --node-address connect.akave.ai:5500
```
If `--account` is not provided, and at least one wallet exists, the first wallet in the keystore will be used.

## Using `--private-key` Directly (Advanced/Optional)

The recommended way is to use wallets. However, the `--private-key` flag is still available for advanced flows or automated environments.

{{< callout type="info" >}}
If you must use `--private-key`, avoid typing the raw key in the command line directly. Use a file or environment variable instead as shown below.
{{< /callout >}}

### Approach 1: Private Key File

1. Create a secure directory and file:

```bash
mkdir -p ~/.key
echo "your-private-key-content" > ~/.key/user.akvf.key
chmod 600 ~/.key/user.akvf.key
```
2. Use it in commands:

```bash
akavecli bucket create mybucket \
    --private-key "$(cat ~/.key/user.akvf.key)" \
    --node-address connect.akave.ai:5500
```
### Approach 2: Environment Variable

1. Set the variable for the current session:

```bash
export AKAVE_PRIVATE_KEY="<your-private-key>"
```

2. Use it in commands:

```bash
akavecli bucket create mybucket \
    --private-key "$AKAVE_PRIVATE_KEY" \
    --node-address connect.akave.ai:5500
```
3. Clear when done:

```bash
unset AKAVE_PRIVATE_KEY
```

If you add the `export` line to your shell RC (`~/.bashrc` or `~/.zshrc`), it will be available in every new shell session. Be sure your machine is secure and not shared if you choose this approach.

## Next Steps

Now that you have completed the wallet setup, you can proceed to [Bucket and File Commands]({{< relref "akave-sdk-cli/akavecli-bucket-file.md" >}}) for bucket and file management.