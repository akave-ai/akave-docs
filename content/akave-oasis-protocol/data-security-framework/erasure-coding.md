---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: 'Erasure Coding'
weight: 3
cascade:
  type: docs
---
Read First: [Our Data Security Framework](https://docs.akave.xyz/akave-oasis-protocol/data-security-framework/)

## Intro

Erasure Coding (EC) is a data protection technique that ensures our data remains safe even if some parts of it are lost. Instead of simply copying data for backup, EC intelligently breaks it into smaller pieces and adds extra recovery data, so that missing parts can be recreated.

Imagine you have a **puzzle with 32 pieces**. Normally, if you lose a few pieces, the puzzle remains incomplete. With EC, you can create **16 extra puzzle pieces** based on the original 16, so even if some pieces are lost, you can still complete the puzzle. This redundancy helps in preventing data loss.

## Overview

**Akave's Erasure Coding** is a data protection method that splits data into fragments and distributes them across multiple storage nodes. By **adding parity fragments**, Akave ensures that data can be reconstructed even if some fragments are lost or corrupted. This approach combines data resilience with efficient storage utilization.

## Key Components

1. **Data Splitting (chunking)**

    - As part of Akave's data security framework, the platform implements data chunking. Before encryption, original files are disassembled into smaller, more manageable pieces, similar to a complex jigsaw puzzle. These fragments are then distributed across Akave's decentralized network and replicated onto Filecoin, ensuring robust security and redundancy.

        - *Chunking Process:*

            - Files are divided into chunks, typically 32 MB in size.
            - Each chunk is further subdivided into smaller data blocks (up to 1 MB) for optimized processing and distribution.

    - This dispersion strategy means that the pieces of a file reside in separate, distinct locations, making unauthorized reassembly virtually impossible. Even if an intruder were to gain access to a single fragment, without the rest and the unique cryptographic keys, it remains an unsolvable riddle.

2. **Reed-Solomon Algorithm**

    - Akave employs the Reed-Solomon error correction algorithm to generate parity blocks for each data block.
    - Parity blocks provide redundancy, enabling data recovery even if a subset of the original and parity blocks is unavailable.

3. Network Distribution

    - Data and parity blocks are distributed across a network of storage nodes.
    - Nodes are geographically dispersed to enhance reliability and reduce the risk of data loss from localized failures.
    - In addition, each storage node replicates the data blocks to the Filecoin network. This ensures an additional layer of resiliency and decentralization by leveraging Filecoin’s distributed storage capabilities, providing further protection against data loss or corruption.

4. Data Sampling and Mini-Proving

    - Akave performs periodic data sampling and mini-proving on stored data blocks to verify their integrity.
    - If a storage node becomes unavailable, these mechanisms identify missing or corrupted data blocks.
    - The system then triggers a process to rebuild the missing data blocks using the Reed-Solomon algorithm, ensuring uninterrupted data availability.


## Process Flow

1. **Data Chunking**

    - A file is split into fixed-size chunks, which are further divided into smaller data blocks.

2. **Parity Generation**

    - Each set of data blocks is processed using the Reed-Solomon algorithm to produce parity blocks.
    - Example: For every **x** data **blocks**, **n parity blocks** are generated, achieving a **x+n-block** total.

3. **Distribution**

    - Data and parity blocks are distributed across multiple storage nodes in the network.
    - Each node also replicates the data blocks to the Filecoin network for enhanced reliability and durability.

4. **Recovery**

    - During retrieval, available data blocks and parity blocks are collected.
    - The Reed-Solomon algorithm reconstructs missing data blocks, ensuring data integrity.
    - Data sampling and mini-proving mechanisms help proactively identify and rebuild missing data blocks before they impact data availability.


## Security and Reliability Contributions

- **Resilience**: Data can be recovered even if several storage nodes are unavailable.
- **Efficiency**: Minimizes storage overhead while providing strong fault tolerance.
- **Scalability**: Easily adapts to increasing data volumes and node numbers.
- **Enhanced Reliability**: Filecoin replication provides a secondary layer of protection against data loss, ensuring long-term availability and security.
- **Proactive Integrity Verification**: Data sampling and mini-proving ensure that data integrity issues are identified and resolved promptly.


## Example policy

### How Our EC Policy Works (Simplified Explanation)

- Every file is **split into 32 MB chunks**.
- Each **32 MB chunk is further divided into 32 DataBlocks**, with each DataBlock being **1 MB**.
- **16 of these blocks store the actual data**.
- **The other 16 blocks store recovery (parity) data**.
- If some of the 32 DataBlocks go missing, the system can **rebuild the lost data using the 16 recovery DataBlocks**.
- This ensures data is safe even if storage failures occur.

This setup means that for every **32 MB of original data, we store an additional 32 MB of parity**, resulting in **100% overhead**. (This is configurable through our SDK)


## Technical Breakdown (Deep Dive)

### Chunk Size & Structure

- A chunk consists of 32 DataBlocks (typically 1 MB each, totaling 32 MB per chunk).
- When EC is enabled, 16 DataBlocks are data, and 16 DataBlocks are parity.
- This matches the code constraint:

```go
if s.parityBlocksCount > s.streamingMaxBlocksInChunk/2 {
    return nil, errSDK.Errorf("parity blocks count %d should be <= %d", s.parityBlocksCount, s.streamingMaxBlocksInChunk/2)
}
```

### EC Schema

- **Formula**: `n (total) - k (data) = m (parity)`
- In our case: `32 (total) - 16 (data) = 16 (parity)`
- **Expansion Factor**: 2x (100% overhead), meaning we **store double the original data size**.

### 256 MB File Example

1. **Chunking:**

- A 256 MB file is divided into **8 chunks**, each **32 MB**.
- Since only **16 DataBlocks per chunk store actual data**, we read **16 MB at a time**.
- `256 MB / 16 MB = 16 chunks`.

2. **Applying EC:**

- Each chunk (32 DataBlocks) gets **16 DataBlocks** and **16 parity blocks**.
- **Total number of blocks in the system: 16 chunks × 32 DataBlocks = 512 DataBlocks**.
- **Total storage used:** `512 MB` (instead of 256 MB), confirming `100% overhead`.


## Storage Redundancy and Node Requirements

- **Each chunk (32 DataBlocks) must be stored across 32 independent storage units (nodes)**.
- **A single node failure results in losing only 1 DataBlock, ensuring fault tolerance**.
- Regardless of total file size, the network **requires at least 32** nodes to distribute blocks properly.


## Our EC Policy, Overhead, and Redundancy

### EC Policy:

- We use **Reed-Solomon Erasure Coding** with a **16 data, 16 parity configuration (n=32, k=16, m=16)**.
- EC is applied at the **chunk level (32 DataBlocks per chunk, 1 MB per DataBlock)**.

### Overhead:

- **100% storage overhead** (i.e., storing **2x the original data size** due to parity blocks).
- **For every 256 MB of data, the actual stored size is 512 MB**.

### Redundancy & Resilience:

- **Data is safe as long as at least 16 out of 32 DataBlocks are available**.
- **Requires at least 32 nodes** to store blocks separately for full fault tolerance.
- **If up to 16 DataBlocks are lost, data remains intact and always recoverable**.

This setup ensures **high data durability and resilience**, even in the case of multiple failures.