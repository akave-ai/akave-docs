---
date: '2025-04-30T23:41:52-05:00'
draft: false
title: 'Akave o3 Hosted'
weight: 6
cascade:
  type: docs
---

Akave.Cloud  `The Hosted Version of O3`  provides a fully managed deployment of the O3 API, enabling developers and enterprises to leverage decentralized storage without managing infrastructure.

![Akave o3 Self-Hosted vs Akave.cloud](/images/hosted-self-hosted.png)
*Akave o3 Self-Hosted vs Akave.cloud*

### Key Features

- **Hosted O3 API with Full S3 Compatibility**  
  Use the O3 endpoint without needing to run your own instance. Compatible with AWS CLI and SDKs.

- **Managed Key Infrastructure**  
  Akave handles authentication and secure key storage, simplifying access control and permissions management.

- **Portability and Flexibility**  
  You can migrate your Akave.Cloud deployment to your own environment at any time. Simply import your private key to access your data through a self-hosted setup with no disruption.

### Ideal For:

- Teams that want a plug-and-play decentralized storage experience.
- Enterprises that need secure access without managing nodes or keys.
- Developers onboarding quickly into the Akave network.

Akave.Cloud also serves as a blueprint for **service providers** to run their own O3-powered subnets and build custom services for businesses.


## Key Management in Akave.Cloud

For Akave.Cloud users, key management is handled as a managed service:

- **Private keys and access credentials** are stored using secure enclave mechanisms like **HSMs** or **MPC-based signing** (planned roadmap).
- **Encryption keys** remain client-side to preserve zero-trust principles. (planned roadmap)
- Akave will provide support for **delegation, rotation, and revocation** of keys via smart contracts (in development).
- Future integration with **Lit Protocol** will enable decentralized key governance, threshold access policies, and time-based access controls.

This approach allows enterprises to adopt decentralized storage **without compromising security, usability, or compliance**.