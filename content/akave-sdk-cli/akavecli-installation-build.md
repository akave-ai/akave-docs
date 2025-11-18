---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Install and Build the Akave CLI'
weight: 30
cascade:
  type: docs
---

This page explains how to install and build the **Akave CLI (`akavecli`)** from source. Make sure you have completed the [prerequisites]({{< relref "akave-sdk-cli/akavecli-prerequisites.md" >}}) before proceeding.

## 1. Clone the Repository

To install the Akave CLI, start by cloning the repository and navigating to the directory created (`akavesdk/`):

```bash
git clone https://github.com/akave-ai/akavesdk.git
cd akavesdk
```
## 2. Build the CLI

To build the CLI, run the below command from the root of the repository (`akavesdk/`):

```bash
make build
```

This produces the CLI binary at `bin/akavecli` under the root.

## 3. Make the Binary Available System-Wide

To run `akavecli` from any directory, move it into a directory on your `PATH` by running one of the below commands from the root of the repository (`akavesdk/`).

For macOS, Ubuntu, Debian, and other other Unix-Based Systems (CentOS, Fedora, etc.) run:

```bash
sudo mv bin/akavecli /usr/local/bin/
```

If `/usr/local/bin` is not in your `PATH`, you may use `/usr/bin`, though `/usr/local/bin` is preferred for user-installed tools:

```bash
sudo mv bin/akavecli /usr/bin/
```

## 4. Verify the Installation

Run:

```bash
akavecli version
```

You should see the CLI version printed without needing to specify the full path where the binary is located.

If this works, your installation is complete and you can proceed to [Wallet Management]({{< relref "akave-sdk-cli/akavecli-wallet.md" >}}) for wallet setup.