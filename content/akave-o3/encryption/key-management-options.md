---
date: '2025-04-28T21:41:52-05:00'
draft: false
title: 'Key Management Options'
weight: 15
cascade:
  type: docs
---

# Key Management Options

Managing keys securely is critical when using encryption on Akave O3. You can choose between **self-managed keys** for client-side encryption or **automatic server-side encryption** using the S3-compatible API.

## Server-Side Encryption Keys (SSE)

When using `--sse AES256`, Akave handles the encryption and decryption transparently on the server side. You do not manage the key directly.

- Simple to use
- No need to generate or store keys
- Recommended for general-purpose storage

## Client-Side Key Management

For client-side encryption, you must manage the full lifecycle of your encryption key:

### Best Practices

- Store keys in a secure location (e.g., `.key` directory, environment variables, encrypted vaults)
- Avoid including keys in scripts or CLI history
- Use `chmod 600` to restrict key file access
- Rotate keys regularly and re-encrypt critical data as needed

## File-based Key Usage Example

You can pass the encryption key via environment variable or load it from a secured file:
```bash
export USER_ENCRYPTION_KEY="$(cat ~/.key/encryption.key)"
```
Then use this key during client-side encryption before uploading the file.

## Planned Integration

Akave aims to integrate **Lit Protocol** in the future for:

- Distributed key governance
- Threshold key access
- Time-based or condition-based decryption policies

These features will enhance enterprise key management and unlock smart access scenarios without central key storage.

## Summary

| Encryption Type      | Managed By | Key Location       | Suitable For            |
|----------------------|------------|---------------------|--------------------------|
| Server-side (AES256) | Akave O3   | Transparent         | General use              |
| Client-side          | You        | File / Env Var / HSM| Highly sensitive data    |