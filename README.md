# File Encryption / Decryption Tool

A simple Python project that can **encrypt** and **decrypt** both text and files.

This is a college project I built while learning the basics of how encryption
works in Python. The goal was to take something I read about (keeping data
private) and actually turn it into a small working program.

## The problem I wanted to solve

Every day people and businesses store private information on their computers —
customer details, passwords, ID documents, and so on. If a laptop is stolen or a
file is shared by mistake, anyone can open those files and read everything.

I wanted to build a small tool that solves this in a basic way: take a file (or
some text) and **scramble it** so that it is useless to anyone who does not have
the secret key. The right person can then **unscramble** it whenever they need
it. This is the simple idea behind encryption, and I wanted to actually build it
to understand how it works.

## What does this project do?

In simple words, **encryption** means scrambling a message so that nobody can
read it unless they have the secret "key". **Decryption** is the opposite —
turning the scrambled message back into the normal readable one.

So this program lets you:

- Encrypt and decrypt **plain text** that you type in
- Encrypt and decrypt **files** stored on your computer
- Choose between **two different methods** (explained below)

## How I approached it (two methods)

While learning, I found there are very simple ciphers and there are proper
secure ones. I decided to include both, because comparing them helped me
understand *why* the simple ones are not safe.

### 1. Caesar Cipher (the "learning" method)

This is one of the oldest and simplest ciphers. It works by shifting every
letter in the alphabet by a fixed number (the key). For example, with a shift
of 3, the letter `A` becomes `D`, `B` becomes `E`, and so on.

I wrote this one **from scratch** myself, because it shows how a cipher
actually works step by step.

> ⚠️ Note: The Caesar Cipher is **not secure** at all and should never be used
> for real data. It is only here to learn the concept.

### 2. Fernet encryption (the "proper" method)

For real, strong encryption I used Python's `cryptography` library, which
gives us something called **Fernet**. Fernet uses a strong, well-tested
encryption method (AES) and handles all the difficult maths for us.

With this method, a secret **key** is generated and you need that same key to
decrypt the data again. This is much closer to how encryption is actually used
in the real world.

## Tools and technology used

- **Python 3** — the programming language
- **cryptography** library — provides the secure Fernet method
- Python's built-in **file handling** (`open`, read/write) for the file parts

## Project structure

```
encryption-decryption-tool/
├── README.md          # this file
├── requirements.txt   # libraries the project needs
├── caesar_cipher.py   # the simple Caesar Cipher (text + files)
├── fernet_cipher.py   # the secure Fernet method (text + files)
└── main.py            # the menu that runs everything
```

## How to install and run it

You need Python 3 installed. Then:

```bash
# 1. install the library this project needs
pip install -r requirements.txt

# 2. run the program
python main.py
```

When it starts you will see a simple menu:

```
====================================
  File Encryption / Decryption Tool
====================================

What would you like to do?
  1. Encrypt text
  2. Decrypt text
  3. Encrypt a file
  4. Decrypt a file
  5. Exit
```

You pick an option, choose the method (Caesar or Fernet), and the program does
the rest.

### Quick example (encrypting text with the Caesar Cipher)

```
Enter your choice (1-5): 1
Enter the text you want to encrypt: Hello World
Choose a method:
  1. Caesar Cipher (simple, just for learning)
  2. Fernet (strong, secure encryption)
Enter 1 or 2: 1
Enter the shift key (a number, e.g. 3): 3

Encrypted text: Khoor Zruog
```

> 🔑 **Important about the Fernet method:** when you encrypt with Fernet, a file
> called `secret.key` is created. You **must keep this file** to decrypt your
> data later. If you lose it, the data cannot be recovered.

## Cybersecurity implications

Building this taught me a few important security lessons:

- **Weak encryption gives a false sense of safety.** The Caesar Cipher *looks*
  like it protects data, but it only has 25 possible keys, so an attacker can
  simply try them all (a "brute-force" attack) and break it in seconds. A weak
  method can be worse than none, because people trust it without reason.

- **Strong encryption needs to be authenticated.** Fernet does not only scramble
  the data, it also checks that it has not been changed. In my testing, trying to
  decrypt with the wrong key gave an `InvalidToken` error instead of returning
  fake data. This stops attackers from tampering with the file.

- **The key is the most important secret.** With strong encryption, the data is
  only as safe as the key. If someone steals the key, they can read everything.
  If you lose the key, the data is gone forever. This is called *key management*
  and it is a real challenge in cybersecurity.

- **Never store secrets in your code or upload them.** That is why this project's
  `.gitignore` file blocks `*.key` files from ever being uploaded to GitHub.
  Hard-coding passwords or keys is one of the most common security mistakes.
