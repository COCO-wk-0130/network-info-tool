import ipaddress

def print_ip_info(ip_input):
    ip = ipaddress.ip_address(ip_input)
    print(f"You entered: {ip_input}")
    print(f"IP Version: {ip.version}")
    print(f"Is Private: {ip.is_private}")
    print(f"Is Global: {ip.is_global}")


def main():
    print("=== Network Info Tool ===")
    try:
        ip_input = input("Enter the IP address: ")
        print_ip_info(ip_input)
    except ValueError:
        print("Invalid IP address entered.")


if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to exit? (yes/no): ").strip().lower() in ("yes", "y"):
            print("Exiting the tool.")
            break