---
date: '2025-04-23T22:48:09-05:00'
draft: false
title: 'Akave Zoning — Data Residency & Geofencing'
linkTitle: 'Zoning'
description: 'Akave Zoning: define data residency rules and geofences to keep data within specific regions for compliance, sovereignty, and latency control.'
weight: 4
cascade:
  type: docs
---
The zoning diagram illustrates how Akave organizes data storage based on geographic zones, which can be useful for geofencing and data localization. Here’s a closer look at each component:

![Akave Zoning / Geofencing](/images/zoning.avif)
*Akave Zoning / Geofencing*

1. #### Akave Zoning
    - Zoning allows data to be stored in specific geographic regions or zones based on requirements like data sovereignty, regulatory compliance, or performance needs.

    - Akave nodes are organized into zones (Zone 1, Zone 2, Zone 3, etc.), where each zone may represent a particular geographic area. Data can be stored within a specified zone, ensuring it doesn’t leave that location.

2. #### Geofencing
    - Geofencing restricts data access or storage to specific locations, which is crucial for regulatory compliance in industries like healthcare or finance. By using zoning, Akave ensures data only resides in permitted regions, meeting privacy and security requirements.

3. #### Akave Oasis
    - **Akave Oasis** is our blockchain concept in the zoning setup, representing a core node that connects different zones and subnets together. The Oasis node coordinates data flow between zones and manages geofencing restrictions, ensuring data storage complies with geographic policies.


## Summary of Key Concepts

- **CID (Content Identifier):** A unique identifier generated based on the content of data, ensuring data integrity. Changes to data result in a new CID, enabling immutable storage.

- **Merkle Tree:** A hierarchical hash structure that verifies data integrity and allows Akave to detect tampering or changes to data stored across nodes.

- **Immutable Storage:** Data stored with a CID is unchangeable. Any modification creates a new CID, preserving the original data’s integrity.

- **Decentralized Storage:** Data is stored across multiple nodes in a network, increasing redundancy and security. No single entity controls the data, enhancing privacy and resilience.

- **Filecoin:** A decentralized storage network used as a backup layer in Akave, ensuring long-term data durability and accessibility through incentives.

- **Zoning and Geofencing:** Akave’s zoning feature allows data to be stored within specific geographic areas, supporting regulatory compliance and data localization requirements.