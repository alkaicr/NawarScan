NawarScan

Professional Multi-threaded TCP Port Scanner
Developed by Ahmed Ben Nawar

📌 Overview

NawarScan is a high-performance multi-threaded TCP port scanner built for:

Penetration Testers

Cybersecurity Students

Lab Environments

Ethical Hackers

The tool focuses on speed, clarity, and professional structure suitable for real-world security testing.

⚠️ For authorized testing and educational purposes only.

🚀 Features

⚡ Multi-threaded scanning engine

🎯 Custom port range support (1–65535)

🛰 Banner grabbing for service detection

⏱ Adjustable timeout control

📊 Execution time measurement

🛡 Input validation and error handling

🧠 How It Works

Creates socket connections to target ports

Uses threading to speed up scanning

Attempts banner grabbing on open ports

Displays results in clean structured format

Measures total execution time

📦 Requirements

Python 3.x

No external dependencies

Works on Linux / Windows / macOS

🛠 Installation
git clone https://github.com/alkaicr/NawarScan.git
cd NawarScan
chmod +x nawarscan.py

▶️ Usage

Basic scan:

python3 nawarscan.py <target>


Custom range:

python3 nawarscan.py <target> <start_port> <end_port>


Example:

python3 nawarscan.py 192.168.1.1 1 1000

📷 Example Output
[+] Scanning Target: 192.168.1.1
[+] Port 22 OPEN  | SSH-2.0-OpenSSH_8.2
[+] Port 80 OPEN  | Apache/2.4.41
[+] Scan Completed in 4.27 seconds

🗺 Roadmap

v1.1

UDP scanning support

Better output formatting

v1.2

Service detection improvements

Export results to file

v2.0

CLI argument parsing (argparse)

Stealth scanning modes

Modular architecture

⚖️ Legal Disclaimer

This project is created strictly for educational purposes and authorized penetration testing.
The developer is not responsible for any misuse.

👨‍💻 Author

Ahmed Ben Nawar
Cybersecurity Enthusiast | Penetration Tester

GitHub:

MIT License
