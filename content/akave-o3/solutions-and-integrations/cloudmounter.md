---
date: '2025-06-11T19:23:35-07:00'
draft: false
title: 'CloudMounter'
weight: 29
cascade:
  type: docs
---

[CloudMounter](https://cloudmounter.net/) is a tool that allows you to mount Akave Network storage as a local file system. This enables you to access your data as if it were stored locally, while still benefiting from the security and accessibility of the Akave Network.

## Pre-requisites

1. **Akave O3 Credentials**
These can be requested by contacting Akave at [Akave Cloud Contact](https://www.akave.cloud/contact).

2. **Install dependencies** (Requirements: CloudMounter)

### CloudMounter Installation Guide

For all latest OS installation instructions go to [https://cloudmounter.net/](https://cloudmounter.net/)

#### Mac OS CloudMounter install example

**If you don’t already have CloudMounter installed, you can install it from the CloudMounter website.**
- Visit [https://cloudmounter.net/downloads-mac.html](https://cloudmounter.net/downloads-mac.html) and download the latest version of CloudMounter for Mac OS.
- Run the downloaded cloudmounter.dmg file and drag the CloudMounter application to your Applications folder.

#### Windows CloudMounter install example

**If you don’t already have CloudMounter installed, you can install it from the CloudMounter website.**
- Visit [https://cloudmounter.net/downloads-win.html](https://cloudmounter.net/downloads-win.html) and download the latest version of CloudMounter for Windows.
- Run the downloaded cloudmounter.exe file and follow the installation instructions.

## Configuration

1. **Open CloudMounter and you should see a window similar to the one below (screenshot taken on Mac OS):**

![CloudMounter](/content/images/cloudmounter.png)

2. **Click on the "Amazon S3" button to add a new S3 compatible storage mount.**

3. **Fill in the following fields:**
- **Name:** The name of the mount.
> You can name this anything you like.
- **Endpoint:** The endpoint of the S3 compatible storage.
> You can find a list of valid endpoints in the Akave O3 documentation under [Akave Environment](/akave-o3/introduction/akave-environment/).
- **Access Key:** Enter the access key ID provided to you by Akave.
- **Secret Key:** Enter the secret access key provided to you by Akave.
- **Bucket:** Enter "/" to mount all your S3 buckets or enter the name of the Akave bucket you want to mount.
> If you don't already have a bucket, you can create a new one using the AWS CLI: [Create, List, Delete Buckets](/akave-o3/bucket-management/create-list-delete-buckets/)

![Akave Mount](/content/images/akave_mount.png)

4. **Click on the "Mount" button to mount the S3 compatible storage.**

You're now able to access your Akave bucket(s) as a local file system! Drag and drop items in and out of the mounted bucket(s) to upload and download files, view images, and more.
