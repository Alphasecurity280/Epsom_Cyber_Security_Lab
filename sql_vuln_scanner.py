#!/usr/bin/env python3
import requests
import sys

print("=" * 50)
print(" EPSOM LABS: SQL INJECTION VULN SCANNER v1.0 ")
print("=" * 50)

if len(sys.argv) != 2:
    print("[!] Usage: ./sql_vuln_scanner.py <target_url>") 
    print("[*] Example: ./sql_vuln_scanner.py http://example.com")
    sys.exit()

target_url = sys.argv[1]

payload = "'"
vuln_url = target_url + payload

print(f"[*] Testing target: {target_url}")
print("[*] Injecting malicious SQL payload...")
print("-" * 50)

try:

    response = requests.get(vuln_url, timeout=5)
    html_content = response.text.lower()

    sql_errors = [
        "you have an error in your sql syntax",
        "warning: mysql_fetch_array",
        "unclosed quotation mark after the character string",
        "postgresql query failed",
        "oracle error"
    ]

    is_vulnerable = False

    for error in sql_errors:
        if error in html_content:
            print(f"[!] ALERT: Target is VULNERABLE to SQL Injection!")
            print(f"[+] Found DB Error Indicator: '{error}'")
            is_vulnerable = True
            break

    if not is_vulnerable:
        print("[-] Target seems SAFE. No common SQL errors detected in response.")

except requests.exceptions.RequestException:
    print("[!] Connection error. Make sure the URL is valid and online.")

print("-" * 50)
print("[*] Vulnerability assessment completed.")
print("=" * 50)
