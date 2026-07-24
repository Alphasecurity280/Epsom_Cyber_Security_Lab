#!/usr/bin/env python3
import os

print("=" * 50)
print("    AUTOMATED NETWORK PING SCANNER v1.0    ")
print("=" * 50)

target_ips = ["120.0.0.1", "8.8.8.8", "10.10.10.164"]

for ip in target_ips:
    print(f"[*] Checking status of [ip]...")
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")

    if response == 0:
        print(f"[+] Host {ip} is ALIVE!")
    else:
        print(f"[-] Host {ip} is DEAD or blocking ICMP.")
    print("-" * 40)

