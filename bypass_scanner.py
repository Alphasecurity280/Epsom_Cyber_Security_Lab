#!/usr/bin/env python3
import scapy.all as scapy
import sys

print("=" * 50)
print("    EPSOM LABS: FIREWALL EVASION SCANNER v1.0    ")
print("=" * 50)

if len(sys.argv) != 3:
    print("[!] Usage: sudo ./bypass_scanner.py <target_ip> <target_port>")
    sys.exit()

target_host = sys.argv[1]
target_port = int(sys.argv[2])

print(f"[*] Targeting: {target_host} on port {target_port}")
print("[*] Crafting spoofed packet (Source port: 53 / DNS)...")

ip_layer = scapy.IP(dst=target_host)

tcp_layer = scapy.TCP(sport=53, dport=target_port, flags="S")

spoofed_packet = ip_layer / tcp_layer

print("[*] sending spoofed SYN packet to bypass firewall...")

response = scapy.sr1(spoofed_packet, timeout=2, verbose=False)

print("\n" + "-" * 40)
if response:
    if response.haslayer(scapy.TCP):
        if response.getlayer(scapy.TCP).flags == 0x12:
            print(f"[+] Port {target_port} is OPEN! (Firewall Bypassed!)")
        else:
            print(f"[-] Port {target_port} is FILTERED or CLOSED.")
else:
    print(f"[-] No response. Packet dropped by firewall or host is dead.")
print("=" * 40)
