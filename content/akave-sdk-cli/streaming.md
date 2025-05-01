---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Streaming'
weight: 11
cascade:
  type: docs
---

The **Akave SDK CLI** (`akavesdk`) is a powerful command-line tool for managing storage and metadata on Akave’s decentralized network. Designed for developers, this SDK enables bucket and file management and efficient file streaming.

{{< callout type="info" >}}
 Blockchain-based data operations are done through the [Blockchain based SDK CLI](https://docs.akave.xyz/akave-sdk-cli/blockchain-integrated/) (preferred)
{{< /callout >}}

Blockchain-based data operations are done through the Blockchain based SDK CLI (preferred)

## Installation
### Requirements
1. **Clone repository**

```bash
git clone https://github.com/akave-ai/akavesdk.git
cd akavesdk
```
2. **Install dependency** (Requirements: Go 1.23.5+)

Go to : [https://go.dev/doc/install](https://go.dev/doc/install)

## Mac OS Go install example
**Mac OS Installation instructions for Go (for all latest OS installation instructions go to https://go.dev/dl/)**

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
## Ubuntu OS Go install example
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
## Test & make binary system wide available
To make the akavesdk binary executable from any location without specifying the full path, you’ll need to move it to a directory in the system's PATH. Here’s how to do it on Ubuntu, macOS, and other Unix-based systems.

1. **Ubuntu/Debian**
On Ubuntu and most Debian-based distributions, you can move the binary to `/usr/local/bin/`, which is a common directory for user-installed binaries.

```bash
sudo mv bin/akavecli /usr/local/bin/
```
2. **macOS**
macOS also uses `/usr/local/bin/` for user-installed binaries. The same command will work:

```bash
sudo mv bin/akavecli /usr/local/bin/
```
3. **Other Unix-Based Systems (e.g., CentOS, Fedora)**
For Red Hat-based distributions like CentOS and Fedora, `/usr/local/bin/` is also typically in the `PATH`, so you can use the same command:

```bash
sudo mv bin/akavecli /usr/local/bin/
```
4. **Alternative Locations (If `/usr/local/bin` is Unavailable)**
On some systems, you might also consider `/usr/bin/`. However, this is usually reserved for system binaries, so `/usr/local/bin/` is preferred. If you must use `/usr/bin/`, you can do so like this:

```bash
sudo mv bin/akavecli /usr/bin/
```
**Verifying the Installation**
After moving the binary, you can confirm it's accessible by all users with:

```bash
akavecli version
```
This command should run without needing the full path, indicating that it’s correctly in the `PATH`.

## Run
{{< callout type="info" >}}
 Make sure the minimum file size is 127 bytes! Keep max size to test at 100MB.
{{< /callout >}}

### Streaming API CLI Commands
The CLI also supports direct interaction with the Akave node for bucket and file operations. These commands are useful for high-performance data transfers but do not use the blockchain-based operations provided by the IPC API.

### File Management with Streaming API
**Node Address**
Public endpoint non-blockchain based network  (`--node-address=connect.akave.ai:5000`)

**Bucket Management Commands**
The streaming API enables efficient file uploads by chunking files and distributing blocks across nodes.

- **List Files:** List all files in a specific bucket.
```bash
akavecli files-streaming list <bucket-name> --node-address=connect.akave.ai:5000
```
- **File Info:** Retrieves metadata of a specific file.
```bash
akavecli files-streaming info <bucket-name> <file-name> --node-address=connect.akave.ai:5000
```
- **Upload File:** Upload a file by specifying a file path.
```bash
akavecli files-streaming upload <bucket-name> <file-path> --node-address=connect.akave.ai:5000
```
- **Download File:** Download a file to a destination folder.
```bash
akavecli files-streaming download <bucket-name> <file-name> <destination-folder> --node-address=connect.akave.ai:5000
```
- **Delete File:** Soft deletes a specific file.
```bash
akavecli files-streaming delete <bucket-name> <file-name> --node-address=connect.akave.ai:5000
```
**Advanced Streaming File API Overview**
The streaming API splits files into chunks (up to 32MB) for efficient uploads across multiple nodes. Files are uploaded through the following steps:

1. **Create File Upload:** Initiates a new file upload with a unique ID.
2. **Upload Chunk:** Each chunk is stored with a receipt for its block locations.
3. **Commit Upload:** Finalizes the file upload, making it available for access.