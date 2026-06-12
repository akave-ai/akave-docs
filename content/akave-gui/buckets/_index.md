---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Bucket Management'
weight: 3
cascade:
  type: docs
---

Buckets are the primary storage containers in Akave Cloud. Create a bucket before uploading files, connecting S3-compatible tools, or using Akave as a storage target for integrations.

## Prerequisites

- **Akave Cloud account**
  - Sign in to [Akave Cloud](https://console.akave.com/).
- **Access Key**
  - You need at least one Access Key before creating a bucket.
  - If you do not have one yet, create it from **Access Keys** in the Akave Cloud sidebar.

{{< callout type="info" >}}
Buckets are created under a selected Access Key. When you use that Access Key with S3-compatible tools, the buckets created with it are available through the same credentials.
{{< /callout >}}

## Bucket Creation

{{< callout type="info" >}}
**Loading State**: When you open Buckets, Akave Cloud loads the bucket list and related Access Key data before showing the table. Wait for loading to finish before creating a bucket or searching.
{{< /callout >}}

### Create a Bucket

1. In Akave Cloud, open **Buckets** from the sidebar.

![Buckets page](/images/gui/buckets/buckets-page.png)

2. Then click **Create new Bucket**.

![Create bucket button](/images/gui/buckets/creation/create-bucket-button.png)

If this is your first bucket, you can also click **Create your first Bucket** from the empty state.

![Create bucket button - main interface](/images/gui/buckets/creation/create-bucket-button-empty.png)

3. In the **Create Bucket** modal, enter a bucket name.

![Create bucket modal](/images/gui/buckets/creation/create-bucket-modal.png)

**Bucket names must:**

- Be globally unique across the Akave Cloud instance.
- Be 3-63 characters long.
- Use lowercase letters, numbers, or hyphens.
- Start and end with a letter or number.

**For example:**

```text
test-project-alpha
```

**Invalid examples:**

```text
-test-bucket      (starts with hyphen)
MyBucket         (contains uppercase)
my_bucket        (contains underscore)
ab               (too short, under 3 characters)
```

4. Select the **Access Key** that should own the bucket.

![Select access key](/images/gui/buckets/creation/select-access-key.png)

5. Click **Create Bucket**.

Akave Cloud closes the modal and shows a **Creation scheduled** notification while the bucket is being created in the background.

6. Wait for the final notification.

When creation succeeds, Akave Cloud shows a **Bucket created** notification and the bucket appears in the bucket list.

If creation fails, Akave Cloud shows an error notification. Common errors include:

- **Bucket name already exists** — Choose a different unique name.
- **Invalid characters** — Use only lowercase letters, numbers, and hyphens.
- **Name too short or too long** — Must be between 3-63 characters.

### Verify the Bucket

After the bucket appears in the table, confirm these values:

- **Name**: The bucket name you entered.
- **Created At**: The creation timestamp.
- **Access Key**: The Access Key associated with the bucket.

![Bucket row](/images/gui/buckets/creation/bucket-row.png)

### After Creating a Bucket

After creating a bucket, you can:

- Open the bucket and upload files.
- Use the selected Access Key with an S3-compatible client.
- Connect the bucket to an integration that supports S3-compatible storage.

{{< callout type="info" >}}
If you plan to use the bucket from an external S3-compatible tool such as the AWS CLI, note the Access Key ID, Secret Access Key, Endpoint URL, and Bucket Name.
{{< /callout >}}

## Bucket Search

Use bucket search in Akave Cloud to quickly find buckets by bucket name or by the Access Key associated with them.

### Search Buckets

1. Open **Buckets** from the sidebar.

![Buckets page](/images/gui/buckets/buckets-page.png)

2. Locate the **Search** field above the bucket list.

![Bucket search field](/images/gui/buckets/search-buckets.png)

3. Enter a bucket name or part of a bucket name.

Search is case-insensitive and updates the bucket list as you type.

![Search by bucket name](/images/gui/buckets/search/search-by-bucket-name.png "Note how the case of the search term does not need to match the case of the bucket name.")

4. You can also search by the **Access Key** associated with a bucket.

This is useful when you have multiple Access Keys and want to find buckets created with a specific key.

![Search by access key](/images/gui/buckets/search/search-by-access-key.png)

5. Review the filtered results.

Matching buckets remain visible in the table or grid, depending on your selected view.

![Filtered bucket results](/images/gui/buckets/search/filtered-results.png "Table view")
![Filtered bucket results](/images/gui/buckets/search/filtered-results-grid.png "Grid view")

6. If no buckets match your search, Akave Cloud shows an empty search result.

![No bucket search results](/images/gui/buckets/search/no-results.png)

### Clear Search

To return to the full bucket list, remove the text from the **Search** field.

![No search results](/images/gui/buckets/search/no-search.png "Note how the search field is empty")

### Searchable Fields

Bucket search currently matches:

- **Bucket Name**
- **Access Key**

{{< callout type="info" >}}
Search filters the bucket list shown in Akave Cloud. It does not modify buckets, credentials, files, or Access Keys.
{{< /callout >}}

### After Finding a Bucket

Once you've located a bucket, you can:

- Open the bucket to view or upload files.
- Copy the bucket name from the bucket row.
- Confirm which Access Key is associated with the bucket.
