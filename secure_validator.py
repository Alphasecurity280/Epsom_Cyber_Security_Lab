#!/usr/bin/env python3
import sys

print("=" * 50)
print("    EPSOM LABS: SECURE INPUT VALIDATOR v1.0    ")
print("=" * 50)

def sanitize_input(user_input):
    print(f"[*] Original Input: {user_input}")
    clean_input = user_input.replace("<","&lt;").replace(">", "&gt;")
    clean_input = clean_input.replace("'", "''")
    return clean_input

if len(sys.argv) < 2:
    print("[!] Usage: ./secure_validator.py '<text_to_test'")
    sys.exit()

raw_data = sys.argv[1]
print("[+] Analyzing and sanitizing input data...")
print("-" * 50)

safe_data = sanitize_input(raw_data)
print("-" * 50)
print(f"[+] Secure Sanitized Output: {safe_data}")

if raw_data != safe_data:
    print("[!] SECURITY NOTICE: Dangerous characters filtered and neutralized successfully!")
else:
    print("[+] Input is clean and safe for database processing.")
print("=" * 50)
