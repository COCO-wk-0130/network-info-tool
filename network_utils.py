import ipaddress
import socket
import threading
from queue import Queue, Empty


def get_usable_hosts(network):
    if network.version != 4:
        raise ValueError("Usable host calculation supports IPv4 only.")

    if network.prefixlen >= 31:
        return network.num_addresses

    return network.num_addresses - 2


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