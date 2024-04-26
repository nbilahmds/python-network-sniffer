# PySniff: Python Network Sniffer

PySniff is a Python script for sniffing network traffic on a specified interface and displaying packet information in a table format.

## Features

- Sniffs network traffic on a selected network interface.
- Prompts the user to select a network interface from the available options.
- Displays packet information, including protocol, source IP, and destination IP, in a table format.
- Provides a user-friendly way to analyze network traffic.

## Requirements

- Python 3.x
- scapy library (`pip install scapy`)
- prettytable library (`pip install prettytable`)
- netifaces library (`pip install netifaces`)

## Usage

1. Clone the repository:

git clone https://github.com/nbilahmds/python-network-sniffer.git

2. Navigate to the repository directory:

cd python-network-sniffer


3. Run the Python script with sudo (requires root privileges):

sudo python3 ns.py


4. Follow the on-screen instructions to select a network interface from the available options.

5. Press Ctrl+C to stop sniffing network traffic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
