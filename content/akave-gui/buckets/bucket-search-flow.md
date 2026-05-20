---
date: '2026-05-20T00:00:00+02:00'
draft: false
title: 'Search Buckets'
weight: 2
aliases:
  - /akave-o3/bucket-management/search-buckets
  - /akave-o3/bucket-management/search-buckets/
cascade:
  type: docs
---

Use bucket search in Akave Cloud to quickly find buckets by bucket name or by the Access Key associated with them.

## Prerequisites

- **Akave Cloud account**
  - Sign in to [Akave Cloud](https://console.akave.com/).
- **Existing buckets**
  - Bucket search works on the buckets already available in your account.

## Search Buckets

1. In Akave Cloud, open **Buckets** from the sidebar.

![Buckets page](/images/gui/buckets/buckets-page.png)

2. Locate the **Search** field above the bucket list.

![Bucket search field](/images/gui/buckets/search-buckets.png)

3. Enter a bucket name or part of a bucket name.

Search is case-insensitive and updates the bucket list as you type.

![Search by bucket name](/images/gui/buckets/search/search-by-bucket-name.png)

4. You can also search by the **Access Key** associated with a bucket.

This is useful when you have multiple Access Keys and want to find buckets created with a specific key.

![Search by access key](/images/gui/buckets/search/search-by-access-key.png)

5. Review the filtered results.

Matching buckets remain visible in the table or grid, depending on your selected view.

![Filtered bucket results](/images/gui/buckets/search/filtered-results.png)

6. If no buckets match your search, Akave Cloud shows an empty search result.

![No bucket search results](/images/gui/buckets/search/no-results.png)

## Clear Search

To return to the full bucket list, remove the text from the **Search** field.

![No search results](/images/gui/buckets/search/no-search.png)

## Searchable Fields

Bucket search currently matches:

- **Bucket Name**
- **Access Key**

{{< callout type="info" >}}
Search filters the bucket list shown in Akave Cloud. It does not modify buckets, credentials, files, or Access Keys.
{{< /callout >}}

## Next Steps

After finding a bucket, you can:

- Open the bucket to view or upload files.
- Copy the bucket name from the bucket row.
- Confirm which Access Key is associated with the bucket.
