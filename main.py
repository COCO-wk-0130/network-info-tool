import ipaddress

print("=== Network Info Tool ===")

while True:
    try:
        ip_input = input("Enter the IP address: ")
        ip = ipaddress.ip_address(ip_input)
        print(f"You entered: {ip_input}")
        print(f"IP Version: {ip.version}")
        print(f"Is Private: {ip.is_private}")
        print(f"Is Global: {ip.is_global}")
    except ValueError:
        print("Invalid IP address entered.")

    if ip_input == "exigt":
        print("Exiting the tool.")
        break
