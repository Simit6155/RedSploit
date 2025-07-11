# ☠️ RedSploit by semih

This is an educational reverse shell builder and listener toolkit developed by [RedSimit](https://github.com/Simit6155). It supports multiple reverse shell clients and allows quick setup for red team operations and ethical hacking labs.

> ⚠️ **Disclaimer:** This tool is for **educational and authorized testing** only. Using it against machines without permission is illegal.

---

## 💻 Features

- 🔨 Reverse Shell Client Generator:
  - [1] Python
  - [2] Rust
  - [3] PowerShell
  - [4] Bash

- 🎧 Reverse Shell Listener:
  - Python-based listener

- 🌐 Git clone automation
- 🧼 Auto clear and update for Kali Linux
- 🎨 Colored CLI with a cool ASCII intro

---

## 🚀 Getting Started

### Requirements

- Kali Linux or Debian-based distro
- `git` installed
- Internet connection
- Python 3

### Installation

```bash
git clone https://github.com/Simit6155/revshell-builder.git
cd revshell-builder
python3 builder.py

    📌 Make sure you are running the script with Python 3.

📦 Usage

Run the script:

python3 builder.py

You will see a menu like:

Available Reverse Shell clients:
  [1] Python     [3] Powershell
  [2] Rust       [4] Bash 

Choose the desired option to download the reverse shell code from the corresponding GitHub repo.
⚠️ Important Configuration Step

Before using the reverse shell payloads, you must edit the IP address and port manually in the downloaded client code:

# Example placeholder in Python client:
HOST = "127.0.0.1"  # ❌ Replace this
PORT = 4444         # ❌ And this

# ✅ With your attack machine IP and desired port:
HOST = "162.163.1.10"
PORT = 1234

    ✅ This applies to all clients (Python, Rust, PowerShell, Bash).

🧪 Python Listener

To install the reverse shell listener:

Type "python" at the prompt

It will automatically clone the listener repo:

https://github.com/Simit6155/python-listenerd

Then run the listener from inside the cloned folder.
❌ Exiting

Press q to exit the program at any time.
🔒 Legal & Disclaimer

This tool is designed for ethical hacking, red teaming, and penetration testing. Use it only in environments where you have explicit permission (e.g., your own lab or with a signed agreement).

You are fully responsible for how you use this tool.
📎 Credits

Made by Simit
Instagram: @redsimit
Discord: https://discord.gg/r3PxFWXTNS
