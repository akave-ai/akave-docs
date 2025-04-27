---
date: '2025-04-26T23:58:37-05:00'
draft: false
title: '🔒 Encryption'
weight: 2
cascade:
  type: docs
---
# Read First: Our Data Security Framework

## Overview

Akave uses robust encryption mechanisms to secure data during storage and transmission. Encryption ensures that data is accessible only to authorized users, preventing unauthorized access and tampering.

## Key Components

- **Master Encryption Key**  
  A user-provided 32-byte AES-256 key serving as the foundation for generating file-specific encryption keys.

- **Derived Encryption Keys**  
  Unique keys created from the Master Encryption Key, combined with identifiers such as bucket and file names.  
  Ensures that each file has a distinct encryption key.

- **File Chunk Encryption**  
  Files are encrypted in chunks to optimize processing and ensure secure storage.

- **Wallet Key**  
  A separate key used for blockchain transactions, ensuring secure access and operations within the Akave ecosystem.

## Process Flow

- **Key Generation**  
  A secure random number generator creates the Master Encryption Key.  
  Derived Encryption Keys are generated using cryptographic functions, combining the Master Key with file identifiers.

- **File Upload Encryption**  
  Files are divided into chunks, and each chunk is encrypted with a Derived Encryption Key.  
  Encrypted chunks are structured into a Directed Acyclic Graph (DAG) using IPFS/UnixFS-like protocols.

- **File Download Decryption**  
  Encrypted chunks are retrieved and decrypted using the corresponding Derived Encryption Key.  
  Decrypted chunks are reassembled to reconstruct the original file.

## Security Contributions

- **Confidentiality**  
  Ensures data is encrypted before leaving the client’s environment.

- **Integrity**  
  Protects data from unauthorized modifications.

- **Granularity**  
  Encrypts data at the chunk level, enhancing security and reducing processing overhead.