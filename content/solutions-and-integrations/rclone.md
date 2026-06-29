---
date: '2025-06-11T19:23:35-07:00'
draft: false
title: 'Rclone'
weight: 24
aliases:
  - /akave-o3/solutions-and-integrations/rclone
  - /akave-o3/solutions-and-integrations/rclone/
cascade:
  type: docs
---

[Rclone](https://rclone.org/) is a command-line program to manage files on cloud storage that enables seamless transitions from one storage platform to another. With Akave's fully S3 compatible API, Rclone can be used to migrate data to and from the Akave Network with ease.

**Below is a short video demo for using Akave O3 with Rclone:**

{{< youtube 4z9J0fo6pOs >}}

## Pre-requisites

1. **Akave O3 Credentials**
   - If you do not already have these, please create them on [Akave Cloud](https://console.akave.com/)

2. **Install dependencies** (Requirements: Rclone)

### Rclone Installation Guide

For all latest OS installation instructions go to [https://rclone.org/install/](https://rclone.org/install/)

#### Mac OS Rclone install example

**If you don’t already have Rclone installed, you can add it with:**
```bash
brew install rclone
```
**If Rclone is installed and you need to upgrade it use:**
```bash
brew upgrade rclone
```
**After installing or upgrading, confirm it's installed using:**
```bash
rclone version
```

#### Ubuntu OS Rclone install example

**Rclone has a simple install script that will install the latest version of rclone.**

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

**After installing or upgrading, confirm it's installed using:**
```bash
rclone version
```

## Configuration
Configure Rclone to use Akave's S3 compatible API, Akave O3. For more information on Rclone S3 configuration, see [Rclone S3](https://rclone.org/s3/).

### Akave O3 Configuration

**Configure Akave O3 for use with Rclone by running:**
```bash
rclone config
```

**Follow these steps to configure a new remote:**

1. **Choose to configure a new remote** 
- Select `"n"`
2. **Name your remote** *You can name this however you like*
```bash
Akave
```

3. **Select storage type**
   - Select `"Amazon S3 Compliant Storage Providers..."`
4. **Select provider**
   - Select `"Any other S3 compatible provider"`

5. **Get AWS credentials from runtime**
```bash
false
```
   - *This can also be true depending on your preferred configuration, just make sure to have your environment credentials configured correctly as described in the [AWS CLI docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html). Leave this as false if you'd prefer to store your credentials with Rclone (recommended).*

6. **Enter Access Key ID**
   Enter the access key ID provided to you by Akave.

7. **Enter Secret Access Key**
   Enter the secret access key provided to you by Akave.

8. **Enter Region**
```bash
akave-network
```

9. **Enter Endpoint**
```bash
https://o3-rc2.akave.xyz
```
> Select the endpoint corresponding to your credentials from the options provided here: [Akave Environment](/akave-o3/introduction/akave-environment).

10.   **Location Constraint**
    Leave blank

11.   **ACL**
    Choose `Default`

12.   **Edit advanced config**
    Choose `No`

13.   **Keep this remote?**
    Choose `Yes`

## Usage
Rclone supports many of the same commands as S3 and the Akave CLI. Below is a partial list of the most commonly used commands. You can find the full list of commands that Rclone supports on their website: [Rclone commands](https://rclone.org/commands/)


**Note**: Replace `Akave` with the name you chose for your remote in the commands below.

### Bucket Commands

- **Create Bucket:**
```bash
rclone mkdir Akave:<bucket-name>
```
- **List Buckets:**
```bash
rclone lsd Akave:
```
- **Delete Bucket:**
```bash
rclone purge Akave:<bucket-name>
```
> **Note:** Since Akave O3 has versioning enabled by default this will only work if you have not uploaded any data into the bucket. If you want to delete a versioned bucket and all of it's contents you must first delete all versions of an object. See [Deleting Object Versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html) for more information.

### File Commands

- **List Files:**
```bash
rclone ls Akave:<bucket-name>
```
- **Upload File:**
```bash
rclone copy <file-path> Akave:<bucket-name> 
```
- **Download File:**
```bash
rclone copyto Akave:<bucket-name>/<file-path> <file-path>
```
- **Delete File:**
```bash
rclone deletefile Akave:<bucket-name>/<file-path>
```

### Data Migration Example

The most common use case for Rclone is to migrate data from one storage platform to another. Here is an example of how to migrate data from AWS S3 to Akave O3 using Rclone:

**1. Create a new remote for AWS S3:**
```bash
rclone config
```

**2. Create a new remote for AWS S3:**

Follow the prompts to create a new remote for AWS S3 which Rclone provides detailed instructions for here:
- **[Rclone S3 Configuration](https://rclone.org/s3/#configuration)**

**3. Migrate data from AWS S3 to Akave O3:**
```bash
rclone sync s3:<bucket-name> Akave:<bucket-name> --progress
```
> The progress flag is optional and will show you the progress of the migration.

**4. After migration, validate the data integrity in your Akave bucket by running:**
```bash
rclone check s3:<bucket-name> Akave:<bucket-name> --size-only
```

**Expected output:**
If successful the output should look something like this (where N is the number of files in your bucket):
```bash
NOTICE: S3 bucket rclone-test: 0 differences found
NOTICE: S3 bucket rclone-test: N matching files
```
>If you see a message saying N hashes could not be checked, this is normal and expected as Akave does not currently support the same hash check mechanism as AWS S3.

## Transfer Flags

The flags below are recommended for improving general transfer performance with Akave O3. Actual results depend on your network throughput, latency, and the number and size of files being transferred.

### Upload Flags

- **`--s3-upload-concurrency`**
  - **Default:** `4`
  - **Recommended:** `64`
  - Increasing the upload concurrency fills more of the available bandwidth, which especially helps when the round-trip time (RTT) is high.

- **`--s3-chunk-size`**
  - **Default:** `200MiB`
  - **Recommended:** `8MiB`
  - Reducing the chunk size allows for greater parallelization, which reduces the dependency on a single stream and makes the transfer more consistent over high-latency links.

- **`--s3-disable-checksum`**
  - **Default:** `false`
  - **Recommended:** `true`
  - Skips the full-file MD5 checksum calculation while still relying on multipart integrity checks. The AWS CLI does not compute and store a full-object MD5 for multipart uploads by default, so `aws s3 sync` does not incur this overhead. Running `rclone copy` without this flag caused a 38-second delay for a single 10GiB test file, while enabling it reduced the start time to under three seconds.

### Download Flags

- **`--multi-thread-streams`**
  - **Default:** `4`
  - **Recommended:** `8`
  - Controls parallel streams within large downloads. Increasing the number of streams lets a single large file use more of the available bandwidth, which helps on high-latency or high-bandwidth links.

### Combined Upload and Download Flags

- **`--transfers`**
  - **Default:** `4`
  - **Recommended:** `8`
  - Transfers up to eight files concurrently, which keeps the pipeline full when moving many files. It has no benefit for a single-file test.

### Combined Example

When running operations that include both uploads and downloads, you can combine all of the flags above. Rclone applies each flag only where it is relevant.

```bash
rclone sync <local-path> Akave:<bucket-name> \
  --transfers 8 \
  --multi-thread-streams 8 \
  --s3-upload-concurrency 64 \
  --s3-chunk-size 8Mi \
  --s3-disable-checksum \
  --progress
```