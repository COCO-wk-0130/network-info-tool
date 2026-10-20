import ipaddress
import socket
import threading
from queue import Queue, Empty

# Shared executor to avoid creating a new thread pool for each lookup

def lookup_hostname(ip, timeout=1):
    result = Queue(maxsize=1)

    def resolve():
        try:
            hostname, aliases, addresses = socket.gethostbyaddr(str(ip))
            result.put((hostname, aliases, addresses))
        except OSError:
            result.put((None, None, None))

    thread = threading.Thread(target=resolve, daemon=True)
    thread.start()

    try:
        return result.get(timeout=timeout)
    except Empty:
        return None, None, None

def parse_ip_input(ip_input):
    if "/" in ip_input:
        interface = ipaddress.ip_interface(ip_input)
        return interface.ip, interface.network
    else:
        ip = ipaddress.ip_address(ip_input)
        return ip, None

def print_subnet_info(network):
    usable_hosts = network.num_addresses

    if usable_hosts > 2:
        usable_hosts -= 2  # Subtract network and broadcast addresses

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