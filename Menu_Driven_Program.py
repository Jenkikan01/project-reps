#!/usr/bin/env python3

ip_addresses = ["192.168.1.1", "192.180.0.1", "10.0.0.5", "200.100.50.1", "10.11.20.1"]
print("   === SOC IP Manager ===")

while True:
    print(f"""
	--- MENU ---
   1. Show IP Address list.
   2. Add IP Address to list.
   3. Remove IP Address from list.
   4. Save list to a file.
   5. Exit""")
    print()
    choice = input("Enter your choice (e.g., 1 - 5): ")
    print()

    if choice == "1":
        for i, ip in enumerate(ip_addresses):
            print(f"   {i + 1}. {ip}")
        print()

    elif choice == "2":
        ip_to_add = input("   Enter IP Address: ")
        ip_addresses.append(ip_to_add)
        print(f"   Added IP Address: {ip_to_add}")
        print()

    elif choice == "3":
        ip_to_remove = input("   Enter IP Address to remove: ")
        if ip_to_remove in ip_addresses:
            ip_addresses.remove(ip_to_remove)
            print(f"   Removed IP Address: {ip_to_remove}")
        else:
            print(f"   {ip_to_remove} not found in the list")
        print()

    elif choice == "4":
        file_name = input("   Enter File Name of your file: ")
        try:
            with open(file_name, "w") as file:
                file.write("--- IP List ---\n")
                for ip in ip_addresses:
                    file.write(f"  {ip}\n")
                file.write("End of file.\n")
            print(f"   List has been saved to {file_name}.")
        except Exception as e:
            print(f"   ERROR: Unexpected {e} when saving the file.")
        print()

    elif choice == "5":
        break
        print("   Program Closed.")

    else:
        print("   Please retry the program again.")

