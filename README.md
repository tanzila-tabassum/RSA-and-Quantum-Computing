# 🔐 RSA Secure Mail System

A command-line application implementing RSA public-key cryptography for secure text communication, with an exploration of post-quantum cryptographic (PQC) techniques.

---

## 📖 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [System Overview](#system-overview)
- [Post-Quantum Cryptography](#post-quantum-cryptography)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

In today's digital era, data privacy and secure communication are paramount. This project implements a simplified yet fully functional **RSA (Rivest–Shamir–Adleman)** encryption and decryption system in Python, enabling users to exchange secure messages.

Beyond the core RSA implementation, the project addresses the emerging threat posed by **quantum computing** — a technology that could render traditional cryptographic systems obsolete. Post-quantum cryptographic (PQC) techniques are explored, along with strategies for transitioning to quantum-resistant encryption models.

### Objectives

- ✅ Design and implement an RSA-based encryption system for secure text communication
- ✅ Reinforce theoretical knowledge through hands-on coding: modular arithmetic, prime validation, and key generation
- ✅ Evaluate RSA's limitations in the context of quantum computing
- ✅ Investigate and propose post-quantum cryptographic methods for near-future secure communication
- ✅ Explore practical integrations such as encrypted mail clients

---

## Features

- 🔑 **RSA Key Pair Generation** — Generate secure key pairs using two user-provided prime numbers
- 🔒 **Encryption** — Encrypt and save text messages using the RSA algorithm
- 🔓 **Decryption** — Decrypt messages using a stored private key
- 💾 **Key & Message Persistence** — Save encryption keys and messages to files for reuse
- 🖥️ **Menu-Driven Interface** — User-friendly, sequential command-line workflow

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- No external libraries required (uses Python standard library)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rsa-secure-mail.git
   cd rsa-secure-mail
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## Usage

When you launch the application, you'll be presented with a menu:

```
===========================
   RSA Secure Mail System  
===========================
1. Generate RSA Key Pair
2. Encrypt a Message
3. Decrypt a Message
4. Exit
===========================
Enter your choice:
```

**Step 1 — Generate Keys:**  
Enter two prime numbers when prompted. The system will compute and save your public and private keys.

**Step 2 — Encrypt:**  
Type your message. It will be encrypted using the public key and saved to a file.

**Step 3 — Decrypt:**  
The system reads the private key and encrypted message from file, and displays the original plaintext.

---

## System Overview

The RSA algorithm relies on the mathematical difficulty of factoring large numbers. This implementation covers:

| Component         | Description                                          |
|-------------------|------------------------------------------------------|
| Key Generation    | Computes `n = p × q`, `φ(n)`, public key `e`, private key `d` |
| Encryption        | Computes ciphertext `c = m^e mod n`                 |
| Decryption        | Recovers message `m = c^d mod n`                    |
| File Persistence  | Keys and messages saved as `.txt` or `.json` files  |

---

## Post-Quantum Cryptography

RSA's security relies on the computational difficulty of integer factorization — a problem that quantum computers (via **Shor's Algorithm**) could solve efficiently. This project includes a discussion and exploration of:

- **Why RSA is vulnerable** to quantum attacks
- **NIST PQC candidates** such as CRYSTALS-Kyber (key encapsulation) and CRYSTALS-Dilithium (digital signatures)
- **Migration strategies** for transitioning existing RSA systems to quantum-resistant alternatives

> 📄 See `Project Report.pdf` for the full post-quantum analysis and findings.

---

## Project Structure

```
RSA Implementation/
├── RSA.py               # Core RSA logic: key generation, encryption & decryption
├── message.txt          # Stores the encrypted message
├── private_key.txt      # Stores the generated private key
├── public_key.txt       # Stores the generated public key
├── Project Report.pdf   # Full project report including PQC analysis
└── README.md
```

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please ensure your code follows PEP 8 style guidelines and includes relevant tests.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

> Built as part of a cryptography and cybersecurity course project. For educational purposes only.
