# Port Scanner

A lightweight Python port scanner that scans for open ports and identifies services. The scanner works across all ports (1-65535) and displays the status of each port with colorful output.

## Features

- Scans all 65535 ports by default (or a specified range)
- Detects open ports and attempts to identify services running on them
- Simple and easy to use
- Colored output for better readability
- Multi-platform support

## Installation Guide

Follow these steps to set up the project on your local machine.

### Step 1: Clone the Repository
First, clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/RoNiXxCybSeC0101/python-portscanner-.git
cd portscanner
```

### Step 2: Set up a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment to isolate dependencies. This ensures that your project dependencies don't interfere with other Python projects on your machine.

#### On Linux/macOS:
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
2. Activate the virtual enviornmet
   ```
   source venv/bin/activate
   ```
### Step 3: Install Dependencies

After setting up your virtual environment (or if you're using your system's Python installation), you need to install the required Python dependencies.

1. Ensure you're in the project directory (where the `requirements.txt` file is located).
2. Install the dependencies listed in `requirements.txt` using the following command:
   ```bash
   pip install -r requirements.txt
   ```
### Step 4: Run the Port Scanner

To use the port scanner, run the script with the target IP address. You can optionally specify a range of ports to scan; if no range is provided, the script will scan all ports from 1 to 65535 by default.

#### Basic Usage:
Run the following command to scan all ports (1-65535) on a target IP address:
```bash
python3 scanner.py <target_ip>
```

Specifying a Port Range (Optional):
If you'd like to scan a specific range of ports, you can provide the start and end port as additional arguments:

bash
Copy code
```
python3 scanner.py <target_ip> <start_port> <end_port>
```

### Example Result 

```
python3 scanner.py 192.168.100.8 1 1000 
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                                                                      

--------------------------------------------------
Target: 192.168.100.8
Port Range: 1-1000
Time Started: 2024-12-05 11:33:29.690912
--------------------------------------------------
[*] Scanning ports...

Scanning Ports:   0%|                                                                           | 1/1000 [00:00<01:47,  9.33port/s][+] Port 80 is open!
    └── Service: HTTP/1.1 400 Bad Request
Date: Thu, 05 Dec 2024 06:03:23 GMT
Server: Apache/2.2.8 (Ubuntu) DAV/2
Connection: close
Content-Type: text/html; charset=iso-8859-1
[+] Port 111 is open!
    └── Service: 
[+] Port 22 is open!
    └── Service: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
Protocol mismatch.
[+] Port 23 is open!
    └── Service: Service not detected
[+] Port 21 is open!
    └── Service: 220 (vsFTPd 2.3.4)
530 Please login with USER and PASS.
[+] Port 25 is open!
    └── Service: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
502 5.5.2 Error: command not recognized
500 5.5.2 Error: bad syntax
Scanning Ports:  46%|████████████████████████████████▎                                      | 455/1000 [00:00<00:00, 2594.64port/s][+] Port 514 is open!
    └── Service: Service not detected
[+] Port 513 is open!
    └── Service: Service not detected
[+] Port 512 is open!
    └── Service: Where are you?
Scanning Ports: 100%|███████████████████████████████████████████████████████████████████████▊| 998/1000 [00:01<00:00, 769.71port/s][+] Port 53 is open!
    └── Service: Service not detected
[+] Port 139 is open!
    └── Service: Service not detected
[+] Port 445 is open!
    └── Service: Service not detected
Scanning Ports: 100%|███████████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 832.73port/s]
--------------------------------------------------
[+] Scan completed at: 2024-12-05 11:33:30.921945
[+] Elapsed Time: 0:00:01.231002
--------------------------------------------------
[+] Open Ports Detected:
    • Port 80: HTTP/1.1 400 Bad Request
Date: Thu, 05 Dec 2024 06:03:23 GMT
Server: Apache/2.2.8 (Ubuntu) DAV/2
Connection: close
Content-Type: text/html; charset=iso-8859-1
    • Port 111: 
    • Port 22: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
Protocol mismatch.
    • Port 23: Service not detected
    • Port 21: 220 (vsFTPd 2.3.4)
530 Please login with USER and PASS.
    • Port 25: 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
502 5.5.2 Error: command not recognized
500 5.5.2 Error: bad syntax
    • Port 514: Service not detected
    • Port 513: Service not detected
    • Port 512: Where are you?
    • Port 53: Service not detected
    • Port 139: Service not detected
    • Port 445: Service not detected
--------------------------------------------------
```
