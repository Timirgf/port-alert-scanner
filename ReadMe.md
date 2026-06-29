# Port Alert Scanner

# Security Note
This project is for educational use and authorized testing only.
Only scan systems you own or have permission to test.

## Overview

Port Alert Scanner is a beginner-friendly Python project that scans a target host to determine whether a TCP port is open or closed.

This project was built to strengthen my understanding of:

* Python programming
* Socket programming
* TCP/IP networking
* Git and GitHub
* Basic cybersecurity concepts

This is **Version 1** of the project and scans **TCP Port 80 (HTTP)**.

---

## Features

* Accepts a target IP address or hostname from the user
* Creates a TCP socket using IPv4
* Attempts to connect to Port 80
* Reports whether the port is **OPEN** or **CLOSED**
* Uses Python's built-in `socket` library

---

## Technologies Used

* Python 3
* Socket Module
* TCP/IP
* IPv4
* Git
* GitHub

---

## Project Structure

```text
port-alert-scanner/
│
├── scanner.py
├── README.md
├── screenshots/
│   ├── version one code running.png
│   └── version1 scanner result.png
└── .gitignore
```

---

## How to Run

Run the program from the project directory:

```bash
python3 scanner.py
```

When prompted, enter an IP address or hostname, for example:

```text
127.0.0.1
```

Example output:

```text
Enter an IP address or website: 127.0.0.1
❌ Port 80 is CLOSED
```

---

## Screenshots

### Version 1 Code

![Version 1 Code](screenshots/version one code running.png)

### Version 1 Scanner Output

![Version 1 Scanner Result](screenshots/version1 scanner result.png)

---

## Skills Demonstrated

* Python programming
* Socket programming
* Network troubleshooting
* TCP communication
* Git version control
* GitHub project management

---

## Security Notice

This project is intended for educational purposes and authorized network testing only.

Only scan systems that you own or have explicit permission to test.

---

## Future Improvements

* Scan multiple ports
* Detect common network services
* Add colorized terminal output
* Log scan results to a file
* Add multithreaded scanning
* Implement an alert system
* Build a graphical user interface (GUI)
