# Network Info Tool

A lightweight Python command-line tool for analyzing IP addresses and displaying useful networking information.

This project is designed to practice Python programming, IP addressing, subnetting, and basic networking concepts.

## Features

**Planned features:**
- Validate IPv4 and IPv6 addresses.
- Identify private, public, and special-purpose IP addresses.
- Display IP address information.
- Calculate IPv4 subnet information using CIDR notation.
- Display network address, subnet mask, broadcast address, and usable host count.
- Perform reverse DNS lookups to retrieve hostnames.
- Handle invalid inputs gracefully.

## Example Usage

Run the program:

```bash
python main.py
```

Example input:

```text
Enter an IP address: 192.168.1.10/24
```

Expected output (planned):

```text
=== Network Info Tool ===

IP Address    : 192.168.1.10
IP Version    : IPv4
Address Type  : Private
Network       : 192.168.1.0/24
Subnet Mask   : 255.255.255.0
Broadcast     : 192.168.1.255
Usable Hosts  : 254
Hostname      : Not found
```

## Requirements

- Python 3.10 or newer
- No third-party Python libraries
- No external APIs

The project uses Python's built-in modules, including:

- `ipaddress` — IP address validation and subnet calculations.
- `socket` — Reverse DNS hostname lookup.

Reverse DNS lookup may require a network connection, but no external web API is used.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/COCO-wk-0130/network-info-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd network-info-tool
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Development Roadmap

- [ ] Initialize the Python project
- [ ] Implement IP address input
- [ ] Validate IPv4 and IPv6 addresses
- [ ] Classify IP addresses
- [ ] Support CIDR notation
- [ ] Calculate subnet information
- [ ] Implement reverse DNS lookup
- [ ] Refactor code into reusable functions
- [ ] Add automated tests
- [ ] Release CLI version 1.0

## Future Improvements

- Graphical user interface (GUI)
- Export results to a file
- Additional networking utilities

## License

License to be determined.