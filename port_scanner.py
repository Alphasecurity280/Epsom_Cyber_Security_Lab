import socket
print("=" * 36)
print("   CYBER PORT SCANNER ACTIVE   ")
print("=" * 36) 
target = input("Enter target IP (e.g. 127.0.0.1):")
ports = [21,22,80,443]
print(f"\n[+] Scanning target: {target}...")
for port in ports:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.settimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"[*]] Port {port}: OPEN (Vulnerable!)")
    else: 
        print(f"[-] Port {port}: CLOSED")

    s.close() 

