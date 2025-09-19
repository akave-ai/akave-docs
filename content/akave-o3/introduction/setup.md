---
date: '2025-04-29T11:41:52-05:00'
draft: false
title: 'Akave O3 setup'
weight: 5
cascade:
  type: docs
---

### Setting Up an AWS CLI Profile for Akave O3

To streamline your workflow, you can configure a dedicated AWS CLI profile for interacting with Akave O3. This allows you to avoid setting environment variables for each session and keeps your credentials organized under a named profile.

### Installation

Before setting up the profile, make sure you have the AWS CLI installed for your operating system using the installation instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Step 1: Configure the Profile

`aws configure --profile akave-o3`

Enter:
- AWS Access Key ID: `<your-access-key>`
- AWS Secret Access Key: `<your-secret-key>`
- Default region name: `akave-network`
- Default output format: `json`

### Step 2: Use the Profile in Commands

```bash
aws s3api list-buckets \
  --profile akave-o3 \
  --endpoint-url https://o3-rc2.akave.xyz
```

You can now run any `AWS CLI` or `s3api` command with `--profile akave-o3` instead of exporting your credentials each time.

> **Note:** Throughout the rest of the documentation, we won’t include the `--profile` flag in every command. It’s up to you whether to use a profile or export credentials manually -- both approaches are supported.
