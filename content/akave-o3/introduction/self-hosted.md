---
date: '2025-04-30T23:41:52-05:00'
draft: false
title: 'Akave o3 Self-Hosted'
weight: 7
cascade:
  type: docs
---

Akave O3 can be deployed as a self-Hosted S3 compatible API in your own infrastructure; on-premises, in the cloud, or at the edge. This gives you full control over storage operations, compliance, and data locality.

![Akave o3 Self-Hosted vs Akave.cloud](/images/hosted-self-hosted.png)
*Akave o3 Self-Hosted vs Akave.cloud*

### Key Benefits

- **Full Control**: Host the O3 S3-compatible API on your own servers or edge devices.
- **Proximity to Compute**: Ideal for low-latency workloads like AI/ML, video processing, and real-time analytics.
- **Data Sovereignty**: Maintain full custody of encryption keys and metadata. No third-party access.
- **Flexible Deployment**: Supports Docker, Docker Swarm, and Kubernetes (coming soon).

### Use Cases

- Regulated industries (finance, healthcare, government)
- Enterprises requiring region-specific data localization
- Developer teams building on edge infrastructure


## Key Management in Self-Hosted O3

When self-hosting, you’re fully responsible for key security and lifecycle management:

- **Client-side encryption**: You provide the encryption key at upload time; it is never stored on the network.
- **Private key management**: Required for interacting with the blockchain (signing transactions, setting ACLs, etc.).
- **Secure storage practices**: Akave encourages best practices for key separation, backup, and rotation. For advanced teams, integration with external HSMs or Lit Protocol is planned on our roadmap for threshold encryption and revocable key policies.