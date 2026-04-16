---
date: '2025-04-29T11:41:52-05:00'
draft: false
title: 'Akave O3 setup'
weight: 5
cascade:
  type: docs
schema_json: |
  {
    "@context": "https://schema.org",
    "@type": "HowTo",
    "name": "Get Started with Akave O3 Sovereign Storage",
    "description": "Connect to Akave O3, your S3-compatible sovereign cloud storage endpoint, using any AWS S3 SDK or tool.",
    "step": [
      { "@type": "HowToStep", "text": "Follow the instructions on this page." }
    ]
  }
---

### Setting Up an AWS CLI Profile for Akave O3

To streamline your workflow, you can configure a dedicated AWS CLI profile for interacting with Akave O3. This allows you to avoid setting environment variables for each session and keeps your credentials organized under a named profile.

{{< callout type="info" >}}
**Important:** Replace `<YOUR_ENDPOINT_URL>` in the examples below with the endpoint URL provided in your [Akave Cloud Console](https://console.akave.com/). Each set of credentials has a specific endpoint URL.
{{< /callout >}}

### Installation

Before setting up the profile, make sure you have the AWS CLI installed for your operating system using the installation instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Step 1: Configure the Profile

`aws configure --profile akave-o3`

Enter:
- AWS Access Key ID: `<your-access-key>`
- AWS Secret Access Key: `<your-secret-key>`
- Default region name: `akave-network`
- Default output format: `json`

You can also edit the credentials file at `~/.aws/credentials` and add the endpoint URL to avoid having to use the `--endpoint-url` flag in every command. Note that this only applies to commands used with the specific profile(s) you have the `endpoint_url` variable listed for.

Use the below command to edit the credentials file:

```bash
nano ~/.aws/credentials
```

Then add the following to the file:

```ini
[akave-o3]
aws_access_key_id = <your_access_key>
aws_secret_access_key = <your_secret_key>
endpoint_url = <YOUR_ENDPOINT_URL>
```

Make sure to save your changes and exit the editor.

### Step 2: Use the Profile in Commands

```bash
aws s3api list-buckets \
  --profile akave-o3 \
  --endpoint-url <YOUR_ENDPOINT_URL>
```

You can now run any `AWS CLI` or `s3api` command with `--profile akave-o3` instead of exporting your credentials each time.

> **Note:** Throughout the rest of the documentation, we won’t include the `--profile` flag in every command. It’s up to you whether to use a profile or export credentials manually -- both approaches are supported.
