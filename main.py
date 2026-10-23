from network_utils import parse_ip_input, get_usable_hosts, lookup_hostname

def print_subnet_info(network):
    usable_hosts = get_usable_hosts(network)

    print("\n---Subnet Information---")
    print(f"Network: {network}")
    print(f"Subnet Mask: {network.netmask}")
    print(f"Broadcast: {network.broadcast_address}")
    print(f"Usable Hosts: {usable_hosts}")

def print_ip_info(ip):
    print(f"You entered: {ip}")
    print(f"IP Version: {ip.version}")
    print(f"Is Private: {ip.is_private}")
    print(f"Is Global: {ip.is_global}")

def main(): 
    print("\n=== Network Info Tool ===")
    try:
        ip_input = input("Enter the IP address: ").strip()
        ip, network = parse_ip_input(ip_input)
        hostname, aliases, addresses = lookup_hostname(ip)

        print_ip_info(ip)

        print(f"Hostname: {hostname or 'Not found / Timed out'}")

        if network is not None:
            if network.version == 4:
                print_subnet_info(network)
            else:
                print("IPv6 subnet calculations are not supported yet.")
    except ValueError:
        print("Invalid IP address or subnet mask.")


if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to exit? (yes/no): ").strip().lower() in ("yes", "y"):
            print("Exiting the tool.")
            break