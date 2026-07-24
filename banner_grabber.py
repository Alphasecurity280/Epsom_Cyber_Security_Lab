#!/usr/bin/env python3
import socket
import sys

print("=" * 50)
print("    Cyber MULTI-PORT SCANNER & GRABBER v2.5    ")
print("=" * 50)

target = input("Enter Target IP or Hostname:")
start_port = int(input("Enter Start Port (e.g.,20): "))
end_port = int(input("Enter End Port (e.g., 25): "))
print(f"\n[*] Scanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port,end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,port))

    if result == 0:
        print(f"[+] Port {port}: OPEN")
        try:
            s.sendall(b"Hello\r\n")
            banner = s.recv(1024)
            print(f" --> banner: {banner.decode().strip()}")
        except Exception:
            print(f" --> Banner: No response from service.")
            print("-" * 40)

    else:
        print(f"[-] Port {port}: CLOSED")
        print("-" * 40)

    s.close()

