---
date: '2025-06-11T19:23:35-07:00'
draft: false
title: 'Akash'
weight: 26
cascade:
  type: docs
---

[Akash](https://www.akash.network/) is a decentralized compute protocol that provides a secure, scalable, and cost-effective way to run and manage compute resources. It allows applications to utilize the Akave O3 decentralized storage endpoints. 

## Prerequisites

- **Akash account**
  - If you do not already have an Akash account, please create one at [Akash](https://console.akash.network/)
- **Akave Cloud Credentials**
  - If you do not already have these, please create them on [Akave Cloud](https://console.akave.ai/)

## Setup Guide

To get started with Akave and Akash, make sure you have access to your Akave:
- Access Key ID
- Secret Access Key
- Endpoint URL

As well as a bucket in Akave to store your data. More information on how to create a bucket can be found in the [Bucket Management](/akave-o3/bucket-management/create-list-delete-buckets/) section of these docs.

### Akash Configuration

Start by opening the Akash Console at: [console.akash.network](https://console.akash.network/)

Then, click on the "Deploy" button.

![Akash Deploy](/images/akash_deploy.png)

Then from the available options you can select "Upload your SDL" and use the example SDL provided here: [akave.yaml](https://github.com/akave-ai/urandom/blob/main/akash/akave.yaml)
- Replace the `AKAVE_ENDPOINT` with the appropriate [Akave Endpoint URL](/akave-o3/introduction/akave-environment/)
- Replace the `AKAVE_BUCKET` with your Akave Bucket Name
- Replace the `AKAVE_ACCESS` with your Akave Access Key ID
- Replace the `AKAVE_SECRET` with your Akave Secret Access Key

**Note:** These are all values in the `env` section of the SDL, and so won't be exposed after deployment.

![Akave SDL](/images/akash_sdl.png)

Next, name your deployment, add funds to the Akash escrow account, then select a provider and deploy. 

![Escrow](/images/akash_escrow.png)

In this example I select the "hurricane" provider from Akash.

![Provider Selection](/images/akash_provider.png)

Once deployed you'll be able to see information on the deployment similar to the one below, which includes a URI to view your deployed service. 
{{< callout type="info" >}}
Note that the deployment may take a few minutes to fully initialize and become available.
{{< /callout >}}

![Deployment Details](/images/akash_details.png)

## Usage

For the example SDL provided above this creates a service that interacts with the Akave O3 endpoint at the URI shown. You can use this URI to see objects uploaded to your Akave bucket, as well as access those objects with pre-signed URLs. The SDL uploads an object to the bucket as part of the deployment process, demonstrating that the integration is working correctly. 

You can verify the object was uploaded by checking your Akave bucket using standard [object management commands](/akave-o3/object-management/upload-download-delete-objects/).

This basic deployment demonstrates how to launch an Akash instance which interacts with Akave storage and uses the AWS CLI to:
- [Initialize the storage connection](/akave-o3/introduction/setup/#step-1-configure-the-profile)
- [Upload an object to the bucket](/akave-o3/object-management/upload-download-delete-objects/#upload-an-object)
- [List objects in the bucket](/akave-o3/object-management/upload-download-delete-objects/#list-objects)
- [Generate pre-signed URLs for objects](/akave-o3/presigned-urls/generate-and-use-presigned-urls/)

![Deployed](/images/akash_akave.png)

To add additional functionality modify the SDL using:
- [The O3 section of our docs](/akave-o3/)
- [The AWS boto3 library](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [The AWS JavaScript library](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started.html)
- Additional AWS compatible libraries and tools depending on your specific use case