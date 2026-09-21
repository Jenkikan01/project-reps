#!/usr/bin/env python3

print("=== SOC IP List Processor ===\n")

ip_addresses = ["192.168.1.1", "10.0.0.5", "172.16.0.1", "192.168.1.105", "10.0.0.15"]

print(f"Initial IP List (Total: {len(ip_addresses)}):")

for index, ip in enumerate(ip_addresses, start=1):
    print(f"  {index}. {ip}")
print()
ip_to_add = int(input("Enter number of IP Addresses you want to add: "))

for index in range(ip_to_add):
    new_ip = input(f"Enter IP Address #{index + 1}: ")
    ip_addresses.append(new_ip)
    print(f"IP Address added to list: {new_ip}")

print()
print(f"New IP List (Total: {len(ip_addresses)}):")

for index, ip in enumerate(ip_addresses, start=1):
    print(f"  {index}. {ip}")
print()
print(f"""--- SUMMARY STATISTICS ---
Total IP Addresses: {len(ip_addresses)}
First IP Addresses: {ip_addresses[0]}
Last IP Addresses: {ip_addresses[-1]}
""")

