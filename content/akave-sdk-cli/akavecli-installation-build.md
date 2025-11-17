---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Install and Build Akave CLI'
weight: 30
cascade:
  type: docs
---

This page explains how to install and build the **Akave CLI (`akavecli`)** from source.

## 1. Clone the Repository

    git clone https://github.com/akave-ai/akavesdk.git
    cd akavesdk

## 2. Build the CLI

From the repository root:

    make build

This produces the CLI binary at:

    bin/akavecli

## 3. Make the Binary Available System-Wide

To run `akavecli` from any directory, move it into a directory on your `PATH`.

### Ubuntu / Debian

    sudo mv bin/akavecli /usr/local/bin/

### macOS

    sudo mv bin/akavecli /usr/local/bin/

### Other Unix-Based Systems (CentOS, Fedora, etc.)

    sudo mv bin/akavecli /usr/local/bin/

If `/usr/local/bin` is not in your `PATH`, you may use `/usr/bin`, though `/usr/local/bin` is preferred for user-installed tools:

    sudo mv bin/akavecli /usr/bin/

## 4. Verify the Installation

Run:

    akavecli version

You should see the CLI version printed without needing to specify the full path.

If this works, your installation is complete and you can proceed to:

- {{< relref "akavecli-wallet.md" >}} for wallet setup
- {{< relref "akavecli-bucket-file.md" >}} for bucket and file operations