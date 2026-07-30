#!/usr/bin/env python3
import requests
import sys
import os

print("=" * 50)
print("    EPSOM LABS: ADVANCED WEB DISCOVERER v2.0    ")
print("=" * 50)

if len(sys.argv) != 2:
    print("[!] Usage: ./web_discoverer.py <target_url>")
    print("[*] Example: ./web_discoverer.py http://example.com")
    sys.exit()

target_url = sys.argv[1]
wordlist_path = "wordlist.txt"

if not os.path.exists(wordlist_path):
    print(f"[!] Error: {wordlist_path} not found in this directory!")
    sys.exit()

print(f"[*] Scanning URL: {target_url}")
print(f"[*] Loading wordlist from: {wordlist_path}...")
print("-" * 50)

try:

    with open(wordlist_path, "r") as file:
        for line in file:

            directory = line.strip()

            if not directory:
                continue

            full_url = f"{target_url}/{directory}"

            try:
                response = requests.get(full_url, timeout=3)

                if response.status_code == 200:
                    print(f"[+] FOUND: {full_url} Status: 200 OK)")
                elif response.status_code == 403:
                    print(f"[!] FORBIDDEN: {full_url} (Status: 403 Access Denied)")
            except requests.exceptions.RequestException:

                continue

except requests.exceptions.ConnectionError:
    print("[!] Major connection error. Make sure the URL is online.")
    sys.exit()

print("-" * 50)
print("[*] Scan completed successfully.")
print("=" * 50)
