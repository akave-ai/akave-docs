---
date: '2025-04-29T11:41:52-05:00'
draft: false
title: '📋 Akave o3 environment'
weight: 4
cascade:
  type: docs
---

**Akave O3** offers multiple decentralized endpoints to interact with different layers of the network — including blockchain-backed metadata operations and high-performance streaming storage APIs. These environments are designed to mirror traditional cloud regions for familiar configuration, while operating on decentralized infrastructure.

Below is a summary of currently supported Akave O3 regions and endpoints:

| **Region**        | **Purpose**                      | **API Type**         | **Endpoint URL**                      |
|---------------|------------------------------|------------------|-----------------------------------|
| us-south-1    | Blockchain IPC + Metadata    | IPC / JSON-RPC   | https://o3-rc1.akave.xyz          |
| us-central-1  | High-speed Object Streaming  | S3-Compatible    | https://o3-rc2.akave.xyz          |

**Optional:** You can use `akave-network` as the region value in AWS SDK/CLI configurations to refer to Akave's decentralized S3 interface:

```bash
AWS_DEFAULT_REGION=akave-network
```
These endpoints support both local testing and production deployment. You can plug them into your existing AWS-compatible tooling (CLI, SDKs, Terraform) with minimal changes.