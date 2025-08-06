#!/usr/bin/env python

import socket
import subprocess
import sys
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Clear screen (cross-platform)
subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

# Function to check if host is up
def is_host_up(host, port=80, timeout=2):
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except (socket.timeout, socket.error):
        return False

# Input: remote host
remote_host = input(Fore.CYAN + "Enter a remote host to scan (e.g., scanme.nmap.org): ")
try:
    remote_ip = socket.gethostbyname(remote_host)
except socket.gaierror:
    print(Fore.RED + "Hostname could not be resolved. Exiting.")
    sys.exit()

# Check host availability
if not is_host_up(remote_ip):
    print(Fore.RED + "Host is down or unreachable. Exiting.")
    sys.exit()

# Input: port range
try:
    start_port = int(input(Fore.CYAN + "Enter the start port (1-65535): "))
    end_port = int(input(Fore.CYAN + "Enter the end port (1-65535): "))
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
        raise ValueError
except ValueError:
    print(Fore.RED + "Invalid port range. Exiting.")
    sys.exit()

# Input: socket timeout
try:
    timeout_val = float(input(Fore.CYAN + "Enter timeout in seconds (e.g. 0.5): "))
    if timeout_val <= 0:
        raise ValueError
except ValueError:
    print(Fore.RED + "Invalid timeout value. Exiting.")
    sys.exit()

# File to save results
filename = f"scan_results_{remote_host.replace('.', '_')}.txt"

# Display banner
print(Fore.YELLOW + "_" * 60)
print(f"Scanning {remote_ip} from port {start_port} to {end_port} with timeout {timeout_val}s...")
print("_" * 60)

# Start time
start_time = datetime.now()

# Port scan function
def scan_port(ip, port, timeout_val):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout_val)
            result = sock.connect_ex((ip, port))
            return port, (result == 0)
    except Exception:
        return port, False

# Open file for writing results
with open(filename, "w") as file:
    file.write(f"Port Scan Results for {remote_host} ({remote_ip})\n")
    file.write(f"Port Range: {start_port} to {end_port}\n")
    file.write(f"Scan Timeout: {timeout_val} seconds\n")
    file.write(f"Start Time: {start_time}\n\n")

    # Use ThreadPoolExecutor for concurrency
    with ThreadPoolExecutor(max_workers=100) as executor:
        tasks = [executor.submit(scan_port, remote_ip, port, timeout_val) for port in range(start_port, end_port + 1)]
        for future in as_completed(tasks):
            port, is_open = future.result()
            status = "Open" if is_open else "Closed"
            status_color = Fore.GREEN if is_open else Fore.RED
            print(status_color + f"Port {port}: {status}")
            file.write(f"Port {port}: {status}\n")

    # End time and duration
    end_time = datetime.now()
    duration = end_time - start_time

    # Final log
    file.write(f"\nScan Completed at: {end_time}\n")
    file.write(f"Total Duration: {duration}\n")

print(Fore.CYAN + f"\nScan completed in: {duration}")
print(Fore.YELLOW + f"Results saved to: {filename}")
