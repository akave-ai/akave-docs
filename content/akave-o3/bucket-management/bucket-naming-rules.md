---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Bucket Naming Rules'
weight: 6
cascade:
  type: docs
---

#### Bucket Naming Rules

When creating buckets with Akave O3 (just like with AWS S3), you must follow strict naming conventions to ensure compatibility with DNS-based addressing and routing:

#### Allowed:
- Names must be **globally unique** across the Akave network.
- Must be **between 3 and 63 characters**.
- Can include **lowercase letters, numbers, hyphens (-)**.
- Must **start and end with a letter or number**.

#### Not Allowed:
- **No uppercase letters** or underscores.
- **No IP-style names**, e.g., `192.168.0.1`.
- Cannot contain consecutive periods or dashes (`--`, `..`, `-.`, etc.).
- Cannot start or end with a hyphen or period.
- **No special characters** like `@`, `#`, `!`, etc.

#### Examples:

| ✅ Valid             | ❌ Invalid         |
|---------------------|-------------------|
| akave-logs          | AkaveBucket        |
| my-project-data     | my_bucket          |
| storage123          | 192.168.1.1        |
| abc-123             | -invalid-start     |

> **Tip:** Stick to DNS-friendly lowercase names with hyphens as word separators for best results across tools and SDKs. This is related to [vhs ( virtual host style )](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html) support.