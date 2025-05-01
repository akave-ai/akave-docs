---
date: '2025-04-29T11:41:52-05:00'
draft: false
title: 'What is Akave o3'
weight: 2
cascade:
  type: docs
---

**Akave O3** is the decentralized, S3-compatible storage API built specifically for the Akave ecosystem. It enables developers and enterprises to interact with decentralized storage using the **same familiar AWS S3 API calls**, but without relying on centralized cloud providers. Instead, Akave O3 interfaces directly with a network of decentralized Akave storage nodes, backed by blockchain verification, encryption, and smart contract-based access control.

## Key Features of Akave O3
- **Full S3 API Compatibility**: Akave O3 implements a wide range of AWS S3 operations including bucket creation, object upload/download, multipart uploads, metadata handling, and access control.
- **Decentralized Architecture**: Unlike AWS, Akave O3 connects directly to decentralized Akave Nodes that store encrypted and erasure-coded data across a distributed network.
- **On-Chain Metadata and Access Control**: Every object’s metadata and permissions are managed on-chain, ensuring tamper-proof access control and verifiability without centralized IAM systems.
- **Self-Hosted and Managed Options**: 
  - Users can **self-host** O3 within their datacenters, edge devices, or private clouds.
  - Alternatively, enterprises can use **Akave.Cloud**, a hosted version of O3 for a managed experience with decentralized guarantees.
- **Local Storage Flexibility**: Enterprises and developers can keep storage operations geographically close to compute workloads, enhancing performance, reducing latency, and meeting compliance needs.

## Architectural Highlights
- **Client-Side S3 API**: The O3 client can run in any environment, connecting directly to the decentralized Akave node network.
- **Blockchain-Backed Verification**: All object operations are anchored with blockchain proofs to ensure the integrity and availability of stored data.
- **Programmable Access Control**: Users can define smart contract-based ACLs to manage fine-grained permissions (e.g., MFA access, payment-gated access).
- **Proof of Data Possession (PDP)**: Storage nodes must continuously prove they still hold your data via on-chain cryptographic proofs.
- **Self-Healing Storage**: With erasure coding and distributed replication, Akave O3 ensures data recovery even if multiple nodes fail.

## Why Akave O3?
- **Zero Vendor Lock-In**: Unlike centralized clouds, your data is fully sovereign and portable across storage providers.
- **Transparency and Verifiability**: Full on-chain transparency for access, storage integrity, and object lifecycle.
- **Enterprise Ready**: Seamless migration paths, high performance, customizable zones/geofences, and compliance features for regulated industries.
- **Web3 Native**: Built for integration into decentralized apps (dApps), AI/ML pipelines and DePIN networks.

## Deployment Flexibility
- **Self-Hosted O3**: Ideal for enterprises needing full control, compliance with local data laws, or enhanced privacy.
- **Akave.Cloud Hosted O3**: Perfect for teams that want a plug-and-play decentralized cloud solution without managing infrastructure.

## Example Use Cases
- Enterprise-grade decentralized backup and archiving
- AI/ML pipelines storing training and model state data
- Data sovereignty solutions for governments and regulated industries
- DePIN and decentralized compute projects needing secure, close-to-compute storage