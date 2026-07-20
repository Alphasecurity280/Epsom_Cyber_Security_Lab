import socket
import sys

print("=" * 36)
print("   ADVANCED CYBER SCANNER v2.0   ")
print("=" * 36)
target_input = input("Enter Target Website or IP (e.g. google.com): ") 
try:
   target_ip = socket.gethostbyname(target_input) 
   print(f"[+] Target Hostname Resolved to IP: {target_ip}") 
except socket.gaierror: 
   print("\n[-] Error: Could not resolve hostname. Check connection.") 
   sys.exit()
ports = [21, 22, 80, 443, 23, 25]
print(f"[+] Scanning started on: {target_ip}...\n") 
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port)) 
    if result == 0:
        print(f"[*] Port {port}: OPEN (Vulnerable!)")
    else:
        print(f"[-] Port {port}: CLOSED")
    s.close()
