---
date: '2026-05-20T00:00:00+02:00'
draft: false
title: 'Create a Bucket'
weight: 1
aliases:
  - /akave-o3/bucket-management/create-a-bucket
  - /akave-o3/bucket-management/create-a-bucket/
cascade:
  type: docs
---

Buckets are the primary storage containers in Akave Cloud. Create a bucket before uploading files, connecting S3-compatible tools, or using Akave as a storage target for integrations.

## Prerequisites

- **Akave Cloud account**
  - Sign in to [Akave Cloud](https://console.akave.ai/).
- **Access Key**
  - You need at least one Access Key before creating a bucket.
  - If you do not have one yet, create it from **Access Keys** in the Akave Cloud sidebar.

{{< callout type="info" >}}
Buckets are created under a selected Access Key. When you use that Access Key with S3-compatible tools, the buckets created with it are available through the same credentials.
{{< /callout >}}

## Create a Bucket

1. In Akave Cloud, open **Buckets** from the sidebar.

![Buckets page](/images/gui/buckets/buckets-page.png)

2. Click **Create new Bucket**.

If this is your first bucket, you can also click **Create your first Bucket** from the empty state.

![Create bucket button](/images/gui/buckets/creation/create-bucket-button.png)

![Create bucket button](/images/gui/buckets/creation/create-bucket-button-empty.png)

![Create bucket button](/images/gui/buckets/creation/create-bucket-button-onboarding.png)

3. In the **Create Bucket** modal, enter a bucket name.

Bucket names must:

- Be unique within your account.
- Be 3-63 characters long.
- Use lowercase letters, numbers, or hyphens.
- Start and end with a letter or number.

For example:

```text
test-project-alpha
```

![Create bucket modal](/images/gui/buckets/creation/create-bucket-modal.png)

4. Select the **Access Key** that should own the bucket.

![Select access key](/images/gui/buckets/creation/select-access-key.png)

5. Click **Create Bucket**.

Akave Cloud closes the modal and shows a **Creation scheduled** notification while the bucket is being created in the background.

6. Wait for the final notification.

When creation succeeds, Akave Cloud shows a **Bucket created** notification and the bucket appears in the bucket list.

If creation fails, Akave Cloud shows an error notification with the reason returned by the service.

## Verify the Bucket

After the bucket appears in the table, confirm these values:

- **Name**: The bucket name you entered.
- **Created At**: The creation timestamp.
- **Access Key**: The Access Key associated with the bucket.

![Bucket row](/images/gui/buckets/creation/bucket-row.png)

You can use the search field to find the bucket by name.

![Search buckets](/images/gui/buckets/search-buckets.png)

## Next Steps

After creating a bucket, you can:

- Open the bucket and upload files.
- Use the selected Access Key with an S3-compatible client.
- Connect the bucket to an integration that supports S3-compatible storage.

{{< callout type="info" >}}
If you plan to use the bucket from an external S3-compatible tool, keep the Access Key ID, Secret Access Key, Endpoint URL, and Bucket Name available during setup.
{{< /callout >}}
