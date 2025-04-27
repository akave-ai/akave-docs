---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: '🧩 Erasure Coding'
weight: 3
cascade:
  type: docs
---
# Read First: Our Data Security Framework

## Intro

Erasure Coding (EC) is a data protection technique that ensures our data remains safe even if some parts of it are lost. Instead of simply copying data for backup, EC intelligently breaks it into smaller pieces and adds extra recovery data, so that missing parts can be recreated.

Imagine you have a puzzle with 32 pieces. Normally, if you lose a few pieces, the puzzle remains incomplete. With EC, you can create 16 extra puzzle pieces based on the original 16, so even if some pieces are lost, you can still complete the puzzle. This redundancy helps in preventing data loss.

## Overview

Akave's Erasure Coding is a data protection method that splits data into fragments and distributes them across multiple storage nodes. By adding parity fragments, Akave ensures that data can be reconstructed even if some fragments are lost or corrupted. This approach combines data resilience with efficient storage utilization.

## Key Components

- **Data Splitting (Chunking)**  
  Akave implements data chunking before encryption. Original files are disassembled into smaller pieces and distributed across the network and onto Filecoin for robust security and redundancy.
  
  **Chunking Process:**  
  - Files are divided into chunks, typically 32 MB in size.
  - Each chunk is subdivided into smaller data blocks (up to 1 MB).
  - Dispersed pieces reside in distinct locations, making unauthorized reassembly virtually impossible.

- **Reed-Solomon Algorithm**  
  Akave uses the Reed-Solomon error correction algorithm to generate parity blocks for each data block, enabling data recovery even when a subset is missing.

- **Network Distribution**  
  Data and parity blocks are distributed across geographically dispersed nodes. Each node also replicates data onto Filecoin, ensuring high resiliency.

- **Data Sampling and Mini-Proving**  
  Akave periodically verifies data blocks using sampling and mini-proving. If corruption is detected, missing blocks are rebuilt automatically using Reed-Solomon.

## Process Flow

- **Data Chunking**  
  Files are split into fixed-size chunks, then further into smaller data blocks.

- **Parity Generation**  
  Each set of data blocks is processed to produce parity blocks using Reed-Solomon.

- **Distribution**  
  Data and parity blocks are distributed across nodes and replicated to Filecoin.

- **Recovery**  
  During retrieval, available blocks are collected, and any missing ones are reconstructed using parity data.

- **Integrity Checking**  
  Data sampling and mini-proving proactively detect and rebuild missing data blocks.

## Security and Reliability Contributions

- **Resilience**  
  Data can be recovered even if several storage nodes are unavailable.

- **Efficiency**  
  Minimizes storage overhead while maintaining strong fault tolerance.

- **Scalability**  
  Easily adapts to increasing data volumes and storage node numbers.

- **Enhanced Reliability**  
  Filecoin replication provides a secondary layer of protection.

- **Proactive Integrity Verification**  
  Data sampling ensures issues are identified and resolved before impacting availability.

## Example Policy

### How Our EC Policy Works (Simplified)

- Every file is split into **32 MB chunks**.
- Each chunk is divided into **32 DataBlocks** of **1 MB** each.
- **16 DataBlocks** store actual data.
- **16 DataBlocks** store recovery (parity) data.
- If any DataBlocks are lost, the system rebuilds them using the 16 recovery blocks.
- **Storage overhead:** 100% — for every 32 MB of data, 32 MB of parity is added.

### Technical Breakdown (Deep Dive)

- **Chunk Size & Structure**  
  - 32 DataBlocks per chunk (1 MB each).
  - 16 data + 16 parity = 32 blocks total.

- **EC Schema**  
  - Formula: `n (total) - k (data) = m (parity)`
  - In our case: `32 (total) - 16 (data) = 16 (parity)`
  - Expansion Factor: 2x (100% storage overhead).

- **256 MB File Example**  
  - Split into 8 chunks (32 MB each).
  - After applying EC, storage footprint doubles:  
    256 MB → 512 MB total stored.

- **Storage Redundancy and Node Requirements**  
  - Each chunk must be spread across **32 nodes**.
  - Loss of up to **16 blocks** per chunk is tolerated without data loss.

## Our EC Policy, Overhead, and Redundancy

- **EC Policy:**  
  Reed-Solomon Erasure Coding (n=32, k=16, m=16).

- **Overhead:**  
  100% (storage used is double the original data size).

- **Redundancy & Resilience:**  
  Data remains recoverable even if up to 50% of blocks are lost.  
  Requires at least 32 nodes for full distribution.

This setup ensures **high durability, security, and performance** — even under network stress or storage node failures.