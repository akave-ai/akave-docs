---
date: '2025-04-29T11:41:52-05:00'
draft: false
title: 'Akave O3 environment'
weight: 4
cascade:
  type: docs
---

**Akave O3** offers multiple hosted S3 compatible API endpoints to interact with different layers of the network. These environments are designed to mirror traditional cloud regions for familiar configuration, while operating on decentralized infrastructure.

Below is a summary of currently supported Akave O3 regions and endpoints:

| **Region**     | **Purpose**           | **API Type**     | **Endpoint URL**                |
|----------------|------------------------|------------------|----------------------------------|
| us-south-1     | Blockchain IPC API     | S3-Compatible    | https://o3-rc2.akave.xyz         |

**Optional:** You can use `akave-network` as the region value in AWS SDK/CLI configurations to refer to Akave's decentralized S3 interface:

```bash
AWS_DEFAULT_REGION=akave-network
```
These endpoints support both local testing and production deployment. You can plug them into your existing AWS-compatible tooling (CLI, SDKs, Terraform) with minimal changes.

To authenticate, you’ll need an `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, which can be obtained through our [Telegram Builders Channel](https://t.me/akavebuilders) for testing, or by contacting our sales team for production use at [akave.com/contact](https://akave.com/contact). These credentials allow secure interaction with Akave’s decentralized object storage, just like with traditional AWS services.