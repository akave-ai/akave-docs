---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Blockchain integrated'
weight: 10
cascade:
  type: docs
---

The Akave SDK CLI (`akavesdk`) is a powerful command-line tool for managing storage and metadata on Akave’s decentralized network. Designed for developers, this SDK enables bucket and file management, efficient file streaming, and blockchain-based data operations through the IPC API.

## Installation

### Requirements

1. **Clone repository**
```bash
git clone https://github.com/akave-ai/akavesdk.git  
cd akavesdk
```
2. **Install dependency** (Requirements: Go 1.23.5+)

Official Documentation: [https://go.dev/doc/install](https://go.dev/doc/install)

<details>
<summary>Go Installation Guide</summary>

### Mac OS Go install example

Mac OS Installation instructions for Go - for all latest OS installation instructions go to [https://go.dev/dl/](https://go.dev/dl/)

**If you don’t already have Go installed, you can add it with:**
```bash
brew install go
```
**If Go is installed and you need to upgrade to version 1.23.5+ use:**
```bash
brew upgrade go
```
**After installing or upgrading, confirm the version:**
```bash
go version
```

### Ubuntu OS Go install example

**Download package, check online for new version if needed.**
```bash
wget https://go.dev/dl/go1.23.5.linux-amd64.tar.gz
```
**Install Go package**
```bash
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.5.linux-amd64.tar.gz
```
**Set path** 
Add to `~/.bashrc`
```bash
export PATH=$PATH:/usr/local/go/bin
```
**After installing or upgrading, confirm the version:**
```bash
go version
```

</details>

## Build

1. **Clone repository**
```bash
git clone https://github.com/akave-ai/akavesdk.git  
cd akavesdk
```
2. **Build the SDK CLI**
```bash
make build  # outputs a CLI binary to bin/akavecli
```

### Test & Make Binary System-Wide Available

To make the `akavesdk` binary executable from any location without specifying the full path, move it to a directory in the system's `PATH`. Here’s how to do it on **Ubuntu, macOS,** and other Unix-based systems.

#### 1. Ubuntu/Debian
On Ubuntu and most Debian-based distributions, you can move the binary to `/usr/local/bin/`, which is a common directory for user-installed binaries.
```bash
sudo mv bin/akavecli /usr/local/bin/
```
#### 2. macOS
macOS also uses `/usr/local/bin/` for user-installed binaries. The same command will work:
```bash
sudo mv bin/akavecli /usr/local/bin/
```
#### 3. Other Unix-Based Systems (e.g., CentOS, Fedora)
For Red Hat-based distributions like CentOS and Fedora, `/usr/local/bin/` is also typically in the `PATH`, so you can use the same command:
```bash
sudo mv bin/akavecli /usr/local/bin/
```
#### 4. Alternative Location (If `/usr/local/bin` is Unavailable)
On some systems, you might also consider `/usr/bin/`. However, this is usually reserved for system binaries, so `/usr/local/bin/` is preferred. If you must use `/usr/bin/`, you can do so like this:
```bash
sudo mv bin/akavecli /usr/bin/
```

### Verifying the Installation
After moving the binary, you can confirm it's accessible by all users with:
```bash
akavecli version
```
This command should run without needing the full path, indicating that it’s correctly in the `PATH`.

## Run

### Get a Wallet Address and Add the Chain to MetaMask

To start, you’ll need an Akave wallet address. Visit [https://faucet.akave.ai](https://faucet.akave.ai), where you can connect, add the Akave chain to MetaMask, and request funds from the faucet.

![Akave Faucet](/images/faucet.gif)

{{< callout type="warning" >}}
  **Always be careful when dealing with your private key. Double-check that you’re not hardcoding it anywhere or committing it to Git. Remember: anyone with access to your private key has complete control over your funds.**

  Ensure you’re not reusing a private key that’s been deployed on other EVM chains. Each blockchain has its own attack vectors, and reusing keys across chains exposes you to cross-chain vulnerabilities. Keep separate keys to maintain isolation and protect your assets.
{{< /callout >}}

### Blockchain Explorer

[http://explorer.akave.ai](http://explorer.akave.ai)

### Node Address

Public endpoint blockchain-based network: `--node-address=connect.akave.ai:5500`

## IPC API Commands (Preferred)

The IPC API is the recommended approach for interacting with Akave’s decentralized storage. It provides access to Akave’s smart contracts, enabling secure, blockchain-based bucket and file operations. You will need your private key to operate on the network.

{{< callout type="info" >}}
 Export your newly created key! (Example through MetaMask): [link](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/)
{{< /callout >}}

### Bucket Commands

- **Create Bucket:** Creates a new bucket using the IPC API.
```bash
akavecli ipc bucket create <bucket-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **Delete Bucket:** Soft deletes a bucket.
```bash
akavecli ipc bucket delete <bucket-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **View Bucket:** Retrieves details of a specific bucket.
```bash
akavecli ipc bucket view <bucket-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **List Buckets:** Lists all buckets stored in the network.
```bash
akavecli ipc bucket list --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
**To secure your key, you can put it in a keyfile and use this: (temporary until new release)**
```bash
akavecli ipc bucket create <bucket-name> --node-address=connect.akave.ai:5500 --private-key "$(cat ~/.key/user.akvf.key)"
```

### File Commands

{{< callout type="info" >}}
 Make sure the minimum file size is 127 bytes! Keep max size to test at 100MB.
{{< /callout >}}

- **List Files:** Lists all files in a specified bucket.
```bash
akavecli ipc file list <bucket-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **File Info:** Fetches metadata of a specific file.
```bash
akavecli ipc file info <bucket-name> <file-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **Upload File:** Uploads a file to a specified bucket.
```bash
akavecli ipc file upload <bucket-name> <file-path> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **Download File:** Downloads a file from a specified bucket.
```bash
akavecli ipc file download <bucket-name> <file-name> <destination-folder> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
- **Delete File:** Deletes a file from a specified bucket.
```bash
akavecli ipc file delete <bucket-name> <file-name> --node-address=connect.akave.ai:5500 --private-key="your-private-key"
```
> Note: IPC-based commands are highly recommended as they ensure data integrity through blockchain-based operations, making them ideal for decentralized storage use cases.


## Approach to Protect Your Private Key

{{< callout type="info" >}}
 Export key in MetaMask: [link](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/)
{{< /callout >}}

Using `--private-key "$(cat ~/.key/user.akvf.key)"` offers protection because:

1. **Secure Storage:** The private key is stored in a hidden file (e.g., `~/.key/user.akvf.key`) rather than directly on the command line, reducing its visibility.

2. **Prevents Command History Exposure:** If the private key is directly typed in the command, it may be stored in the shell's history file (e.g., `~/.bash_history`). By using a file reference, only the file path is stored in history, keeping the key itself hidden.

3. **File Permissions:** Saving the private key in a file allows you to restrict permissions (using `chmod 600 ~/.key/user.akvf.key`), ensuring only your user can read it.

4. **Ease of Use and Consistency:** You can reuse the stored key across multiple commands without retyping it, making it convenient for automation and reducing the risk of accidental exposure.


## How to Implement This Securely
1. Create and Secure the Private Key File: Save your private key to a secure, hidden directory:

```bash
mkdir -p ~/.key
echo "your-private-key-content" > ~/.key/user.akvf.key
chmod 600 ~/.key/user.akvf.key
```
- `mkdir -p ~/.key` creates the hidden directory if it doesn’t already exist.
- `echo "your-private-key-content" > ~/.key/user.akvf.key` writes the private key to the file.
- `chmod 600 ~/.key/user.akvf.key` restricts access so only your user account can read the file.

2. Example: Use the Command with the Private Key File:  reference the key file in your command:

```bash
akavecli ipc bucket create workshop --private-key "$(cat ~/.key/user.akvf.key)" --node-address connect.akave.ai:5500
```
- This command reads the private key from `~/.key/user.akvf.key`.
- It passes the key to the `--private-key` option for akavecli ipc bucket create.
- The `--node-address` flag specifies the node to connect to.

## Steps to Set Up an Environment Variable for Your Private Key

{{< callout type="info" >}}
 Export key in MetaMask: [link](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/)
{{< /callout >}}

1. Save the Private Key to an Environment Variable Temporarily

You can set the private key as an environment variable in your terminal session. This will store the key in memory for the current session only, and it will not be accessible after you close the terminal.

```bash
export AKAVE_PRIVATE_KEY="$(cat ~/.key/user.akvf.key)"
```
Now, the environment variable AKAVE_PRIVATE_KEY holds the private key securely.

2. Use the Environment Variable in the Command

Modify your command to reference the environment variable instead of reading the key from the file:

```bash
akavecli ipc bucket create workshop --private-key "$AKAVE_PRIVATE_KEY" --node-address connect.akave.ai:5500
```
By referencing `$AKAVE_PRIVATE_KEY`, the command will use the key stored in memory rather than reading it directly from a file each time.

3. Clear the Environment Variable When Done

To remove the key from memory, unset the environment variable once you’re finished:

```bash
unset AKAVE_PRIVATE_KEY
```

## Optional: Add the Environment Variable in Your `.bashrc` or `.zshrc`

If you frequently need the private key across sessions, you can add this line to your `.bashrc` or `.zshrc` file:

```bash
export AKAVE_PRIVATE_KEY="$(cat ~/.key/user.akvf.key)"
```

Then, source the file to load the variable:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

Using this approach keeps your private key secure while making it accessible for the command without exposing it on the command line or in history.
