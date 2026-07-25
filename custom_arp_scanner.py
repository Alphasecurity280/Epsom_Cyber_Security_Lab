#!/usr/bin/env python3
import scapy.all as scapy
import socket

print("=" * 60)
print(" EPSOM LABS: ADVANCED PYTHON WI-FI SCANNER WITH HOSTNAME ")
print("=" * 60)

target_subnet = "10.10.10.1/24"

print(f"[*] scanning local network range: {target_subnet}")
answered_list, unanswered_list = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=target_subnet),timeout=2, verbose=False)

print("\n" + "-" * 75)
print("    IP ADDRESS    |     MAC ADDRESS     |    DEVICE NAME    ")
print("-" * 75)

for send, reply in answered_list:
    device_ip = reply.psrc
    device_mac = reply.hwsrc

    try:
        device_name = socket.gethostbyaddr(device_ip)[0]
    except socket.herror:
        device_name = "Unknown Device"

    print(f" {device_ip:<19} | {device_mac:<22} | {device_name}")

print("-" * 75)
print(f"[*] Total active devices found on Wi-Fi: {len(answered_list)}")
print("=" * 75)
