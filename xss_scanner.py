#!/usr/bin/env python3
import requests
import sys
import os

print("=" * 50)
print("    EPSOM LABS: XSS VULNERABILITY SCANNER v1.0    ")
print("=" * 50)

if len(sys.argv) != 2:
    print("[!] Usage: ./xss_scanner.py <target_url>")
    print("[*] Example: ./xss_scanner.py http://example.com")
    sys.exit()

target_url = sys.argv[1]
payloads_path= "xss_payloads.txt"

if not os.path.exists(payloads_path):
    print(f"[!] Error: {payloads_path} not found in this directory!")
    sys.exit()

print(f"[*] Testing target URL: {target_url}")
print(f"[*] Loading payloads from: {payloads_path}...")
print("-" * 50)

try:

    with open(payloads_path,"r") as file:
        for line in file:
            payload = line.strip()

            if not payload:
                continue
            vuln_url = f"{target_url}{payload}"
            print(f"[*] Injecting payload: {payload}")


            try:
                response = requests.get(vuln_url, timeout=4)

                if payload in response.text:
                    print(f"[!] ALERT: Target is VULNERABLE to XSS!")
                    print(f"[+] Found Reflection for payload: {payload}")
                else:
                    print("[-] Payload was sanitized or blocked by server.")
            except requests.exceptions.RequestException:
                print("[!] WAF block: Taeget dropped connection for this payload.")
                continue

except requests.exceptions.ConnectionErorr:
    print("[!] Major connection error. Make sure the URL is online.")
    sys.exit()

print("-" * 50)
print("[*] XSS vulnerability assessment completed.")
print("=" * 50)

