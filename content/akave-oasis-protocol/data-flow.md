---
date: '2025-04-23T22:48:00-05:00'
draft: false
title: 'Akave Data Flow — How Sovereign Storage Works'
linkTitle: 'Data Flow'
description: 'How data flows through Akave: encryption, erasure coding, distribution across nodes, and continuous integrity verification for 11x9s durability.'
weight: 3
cascade:
  type: docs
---
![Akave DataFlow from File/Data to Filecoin](/images/data-flow.avif)
*Akave DataFlow from File/Data to Filecoin*

In the data flow diagram, we see how files or data are stored through the Akave decentralized storage network and use decentralized storage like Filecoin. Here’s a breakdown:

1. #### File/Data Input

    - Users start with files or data, which they want to securely store in a decentralized manner.

2. #### Akave SDK and S3-Compatible API

    - **Akave SDK:** A software development kit that allows developers to interact with Akave’s storage system easily. It manages data chunking, encryption, and interaction with storage nodes.

    - **S3-Compatible API:** Akave offers an S3-compatible API, meaning users familiar with Amazon S3 storage can interact with Akave’s decentralized storage as if they were working with a traditional cloud storage system.

3. #### Data Chunking and Metadata

    - Data is broken into chunks to optimize for distributed storage. Each chunk is encrypted and it's associated metadata, which includes information about the file and its structure is stored on-chain.

    - Metadata ensures that chunks can be reassembled into the original file, and it helps manage storage across different nodes.

4. #### Storage Nodes and Redundancy

    - Akave utilizes a network of nodes, where each chunk of data is stored. Redundant copies of chunks are created across nodes to increase reliability and prevent data loss.

    - The storage process uses concepts such as **Merkle Trees** and **Content Identifiers (CIDs)** to organize and verify data integrity across nodes.

5. #### Merkle Trees and CIDs

    - **Merkle Tree:** A structure used to verify data integrity. In a Merkle tree, each chunk of data generates a hash. These hashes are combined into parent hashes up the tree, ultimately producing a single root hash that represents the entire data set. If any chunk is modified, the root hash will change, making it easy to detect tampering.

    - **CID (Content Identifier):** A unique identifier for data stored in decentralized storage. CIDs are derived from the content itself, so they remain constant as long as the data doesn’t change. This enables immutable storage, where data cannot be modified without changing its CID, ensuring integrity and authenticity.

6. #### Immutable and Decentralized Storage

    - **Immutable Storage:** Once data is stored with a CID, it is effectively permanent and unchangeable. If changes are needed, a new CID will be generated, representing the updated content. This ensures data remains secure and unaltered.

    - **Decentralized Storage:** Instead of being stored on a single server, data is distributed across a network of nodes. This increases redundancy, enhances security, and prevents data from being controlled or censored by a central authority.

7. #### Filecoin Integration

    - **Filecoin:** A decentralized storage network that incentivizes users to share their unused storage space. Akave integrates with Filecoin as an additional storage layer, providing further redundancy and security for long-term data storage.
    
    - Data chunks can be stored on Filecoin’s storage providers, ensuring they’re accessible even if individual nodes go offline. This additional backup adds another layer of durability to Akave’s decentralized storage system.

### Summary of Key Concepts

- **CID (Content Identifier):** A unique identifier generated based on the content of data, ensuring data integrity. Changes to data result in a new CID, enabling immutable storage.

- **Merkle Tree:** A hierarchical hash structure that verifies data integrity. It allows Akave to detect tampering or changes to data stored across nodes.

- **Immutable Storage:** Data stored with a CID is unchangeable. Any modification creates a new CID, preserving the original data’s integrity.

- **Decentralized Storage:** Data is stored across multiple nodes in a network, increasing redundancy and security. No single entity controls the data, which enhances privacy and resilience.

- **Filecoin:** A decentralized storage network used as a backup layer in Akave, ensuring long-term data durability and accessibility through incentives.

- **Zoning and Geofencing:** Akave’s zoning feature allows data to be stored within specific geographic areas, supporting regulatory compliance and data localization requirements.