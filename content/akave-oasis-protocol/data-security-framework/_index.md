---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Data Security Framework'
weight: 1
cascade:
  type: docs
---
Akave’s data security framework is designed to ensure the confidentiality, integrity, and availability of user and enterprise data through a combination of advanced encryption techniques and erasure coding.  
These technologies work together to protect data against unauthorized access and ensure data reliability, even in the event of hardware or network failures.

[Akave's Encryption Overview](https://docs.akave.xyz/akave-oasis-protocol/data-security-framework/encryption/)

[Akave's Erasure Coding Overview](https://docs.akave.xyz/akave-oasis-protocol/data-security-framework/erasure-coding/)

This image outlines the architecture and processes behind Akave's **encryption** and **erasure coding**, providing a comprehensive view of how data is secured and distributed across the network.

![Akave encryption and erasure coding flow](/images/data-security-framework.avif)
*Akave Encryption and Erasure Coding Flow*

#### 1. Initial Processing

- **Input:** The original file is uploaded to the system.
- **Action:** The file is split into 32 MB chunks for manageable processing.
- **Subdividing:** Each 32 MB chunk is further divided into smaller data blocks, typically no larger than 1 MB, to facilitate efficient handling.

#### 2. Encryption

- **Input:** Data blocks from the initial processing step.
- **Action:** Each data block is encrypted using a unique **Derived Encryption Key**, which is generated from the **Master Encryption Key** and specific file identifiers (e.g., bucket name, file name).
- **Result:** Encrypted data blocks are created, ensuring confidentiality and protection from unauthorized access.

#### 3. Erasure Coding

- **Input:** Encrypted data blocks.
- **Action:**
  - The **Reed-Solomon algorithm** is applied to generate parity blocks for redundancy.
  - **Example:** For every _x_ data blocks, _n_ parity blocks are created, achieving an _x+n_-block set.
- **Proactive Integrity:** Akave performs periodic data sampling and mini-proving to validate block integrity and ensure uninterrupted availability.

#### 4. Network Distribution

- **Input:** Encrypted data blocks and parity blocks.
- **Action:**
  - Blocks are distributed across geographically dispersed storage nodes to enhance reliability.
  - Each node replicates the data blocks to the **Filecoin network**, adding a secondary layer of resiliency and decentralization.
- **Result:** The distributed architecture ensures high availability and fault tolerance even if individual nodes fail.

#### 5. Retrieval

- **Input:** Requests for stored files.
- **Action:**
  - Available data blocks and parity blocks are collected from the network.
  - Missing or corrupted blocks are reconstructed using the Reed-Solomon algorithm.
  - The decrypted blocks are reassembled into the original file.
- **Result:** The original file is restored securely and reliably for the user.