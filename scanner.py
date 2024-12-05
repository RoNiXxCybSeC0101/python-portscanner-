#!/usr/bin/python3

import pyfiglet
import sys
import socket
from datetime import datetime
import concurrent.futures  # For multithreading
from colorama import Fore, Style, init  # For colorful output
import tqdm  # For progress bar

# Initialize colorama
init()

# Display banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(Fore.CYAN + ascii_banner + Style.RESET_ALL)

# Check for proper arguments
if len(sys.argv) < 2:
    print(Fore.RED + "[-] Usage: python3 scanner.py <ip> [start_port] [end_port]" + Style.RESET_ALL)
    sys.exit(1)

# Parse arguments
target = sys.argv[1]
start_port = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end_port = int(sys.argv[3]) if len(sys.argv) > 3 else 65535

# Resolve hostname to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(Fore.RED + f"[-] Unable to resolve host: {target}" + Style.RESET_ALL)
    sys.exit(1)

# Display scan info
print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)
print(Fore.YELLOW + f"Target: {target_ip}")
print(f"Port Range: {start_port}-{end_port}")
print(f"Time Started: {datetime.now()}" + Style.RESET_ALL)
print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)

# Start timer
start_time = datetime.now()

# Define a function to scan a port
def scan_port(port):
    try:
        # Create a socket and set timeout
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout for each connection attempt
            result = s.connect_ex((target_ip, port))  # Connect to the target
            if result == 0:  # Port is open
                try:
                    # Attempt to grab the banner (service info)
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n")  # Send an HTTP request
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "Service not detected"
                return port, True, banner
    except Exception as e:
        pass
    return port, False, None

# Use multithreading to speed up the scan
open_ports = []
print(Fore.CYAN + "[*] Scanning ports...\n" + Style.RESET_ALL)
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # Create a progress bar
    progress = tqdm.tqdm(total=(end_port - start_port + 1), desc="Scanning Ports", unit="port")
    futures = {executor.submit(scan_port, port): port for port in range(start_port, end_port + 1)}
    for future in concurrent.futures.as_completed(futures):
        progress.update(1)
        port, is_open, banner = future.result()
        if is_open:
            open_ports.append((port, banner))
            print(Fore.GREEN + f"[+] Port {port} is open!" + Style.RESET_ALL)
            print(Fore.BLUE + f"    └── Service: {banner}" + Style.RESET_ALL)
    progress.close()

# End timer
end_time = datetime.now()
elapsed_time = end_time - start_time

# Print scan summary
print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)
print(Fore.CYAN + f"[+] Scan completed at: {end_time}" + Style.RESET_ALL)
print(Fore.CYAN + f"[+] Elapsed Time: {elapsed_time}" + Style.RESET_ALL)
print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)

if open_ports:
    print(Fore.YELLOW + "[+] Open Ports Detected:" + Style.RESET_ALL)
    for port, banner in open_ports:
        print(Fore.MAGENTA + f"    • Port {port}: {banner}" + Style.RESET_ALL)
else:
    print(Fore.RED + "[-] No open ports found." + Style.RESET_ALL)

print(Fore.GREEN + "-" * 50 + Style.RESET_ALL)
