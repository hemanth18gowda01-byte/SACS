# 🔐 Secure Authenticated Communication System using RSA Cryptography

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![RSA](https://img.shields.io/badge/Cryptography-RSA-purple?style=flat-square)
![SHA-256](https://img.shields.io/badge/Hashing-SHA--256-yellow?style=flat-square)
![TCP](https://img.shields.io/badge/Transport-TCP%2FIP-green?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-orange?style=flat-square)

---

## Overview

A Python-based **Command Line Interface (CLI)** application that demonstrates secure communication between a sender and a receiver using modern cryptographic principles.

The system combines **RSA Encryption**, **RSA Digital Signatures**, **SHA-256 Hashing**, and **TCP Socket Programming** to provide:

| Property | Description |
|---|---|
| 🔑 Authentication | Verifies sender identity |
| 🔒 Confidentiality | Protects message content |
| ✅ Integrity | Detects message modification |
| 📝 Non-Repudiation | Sender cannot deny sending the message |

> The application can run on different devices connected through a network. By configuring the receiver's IP address and port number, it functions similarly to a lightweight secure messaging application.

---

## Features

- **Authentication** — The sender signs the SHA-256 hash of a file using their RSA private key. The receiver verifies the signature using the sender's public key.
- **Integrity** — SHA-256 hashing ensures that data has not been modified during transmission.
- **Confidentiality** — Messages are encrypted using the receiver's public key and can only be decrypted using the receiver's private key.
- **Secure Transport** — TCP socket programming enables communication between sender and receiver systems.
- **CLI Interface** — Simple and lightweight implementation for learning and demonstrating cryptographic concepts.

---

## System Architecture

### Authentication Phase

```
Sender                                          Receiver
  │                                                │
  ├─ 1. Select file                                │
  ├─ 2. Generate SHA-256 hash                      │
  ├─ 3. Sign hash with Sender's Private Key        │
  ├─ 4. Encrypt signature with Receiver's Pub Key  │
  ├─────────── 5. Transmit ciphertext ────────────►│
  │                                                ├─ 6. Decrypt with Receiver's Private Key
  │                                                ├─ 7. Verify with Sender's Public Key
  │                                                └─ 8. Authentication complete ✓
```

### Confidential Communication Phase

```
Sender                                          Receiver
  │                                                │
  ├─ 1. Encrypt message with Receiver's Pub Key    │
  ├──────────── 2. Transmit over TCP ─────────────►│
  │                                                ├─ 3. Decrypt with Receiver's Private Key
  │                                                ├─ 4. Recover original message
  │◄──────────── 5. Send acknowledgement ──────────┤
```

---

## Project Structure

```
├── crypto.py           # Shared cryptographic functions
│   ├── hashing_file()              # SHA-256 file hashing
│   ├── RSA_digital_signature()     # Sign hash with private key
│   ├── RSA_encryption()            # Encrypt with public key
│   ├── RSA_decryption()            # Decrypt with private key
│   ├── RSA_Decrypted_DS()          # Recover hash from signature
│   └── receiver()                  # Verify + decrypt message
│
├── sender.py           # Client — authentication & message sending
│   ├── Client socket setup
│   ├── Authentication process
│   └── Secure message transmission
│
└── receiver.py         # Server — verification & message receiving
    ├── Server socket setup (localhost:8000)
    ├── Signature verification
    └── Secure message reception
```

---

## Technologies Used

- **Python 3**
- **RSA Cryptography** — modular exponentiation (`pow(m, e, n)`)
- **SHA-256 Hashing** — `hashlib.sha256()`
- **Socket Programming** — `socket` (TCP/IP, localhost:8000)

---

## How to Run

### Step 1 — Start the Receiver

```bash
python receiver.py
```

The receiver binds to `localhost:8000` and listens for an incoming connection.

### Step 2 — Start the Sender

```bash
python sender.py
```

### Step 3 — Enter Details When Prompted

```
Sender Name      :  <your name>
File for Hashing :  <filename>
Secret Message   :  <message>
```

The application will automatically perform:

1. Hash generation (SHA-256)
2. Digital signature creation (RSA private key)
3. Signature encryption (RSA public key)
4. Signature verification on the receiver side
5. Secure message exchange

---

## Running on Different Devices

To use across a network, update the IP address in `sender.py`:

```python
# sender.py
HOST = '192.168.x.x'   # Replace with receiver's IP address
PORT = 8000
```

Ensure both devices are on the same network and the port is open.

---

## Educational Purpose

This project was developed to understand and demonstrate:

- Public Key Cryptography
- RSA Algorithm
- Digital Signatures
- Hash Functions
- Secure Network Communication
- Authentication Protocols

---

## Future Enhancements

- [ ] Graphical User Interface (GUI)
- [ ] Hybrid Encryption (RSA + AES)
- [ ] Multi-user Chat Support
- [ ] Database Integration
- [ ] Real-time Messaging
- [ ] Key Exchange (Diffie Hellman)
      

---

## Author

**Hemanth Gowda A**
**Gmail** = hemanth18gowda01@gmail.com 

Cryptography and Network Security · python developer · Socket Programming and CLI

---

## License

This project is intended for **educational and research purposes**.
Use responsibly and only in authorized environments.
