#from scapy.all import *
#import argparse
#import netifaces
from scapy.all import *
from prettytable import PrettyTable  # Add this import statement
import argparse
import netifaces

# Function to get available network interfaces
# Rest of the code remains the same...


# Function to get available network interfaces
def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces

# Function to prompt user to select a network interface
def select_interface(interfaces):
    print("Available network interfaces:")
    for idx, iface in enumerate(interfaces):
        print(f"{idx + 1}. {iface}")
    selection = input("Select the interface to run the scan (enter number): ")
    try:
        selection = int(selection)
        if 1 <= selection <= len(interfaces):
            return interfaces[selection - 1]
        else:
            print("Invalid selection. Please enter a valid number.")
            return select_interface(interfaces)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_interface(interfaces)

# Function to handle received packets
def packet_handler(pkt):
    if IP in pkt:
        protocol = "UDP" if pkt[IP].proto == 17 else "Unknown"
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst

        # Create a table to display packet information
        table = PrettyTable(["Protocol", "Source IP", "Destination IP"])
        table.add_row([protocol, src_ip, dst_ip])
        print(table)

def main():
    # Get available network interfaces
    interfaces = get_interfaces()

    # Prompt user to select a network interface
    selected_interface = select_interface(interfaces)
    print(f"Selected interface: {selected_interface}")

    # Sniff network traffic on the selected interface
    print("Sniffing network traffic... (Ctrl+C to stop)")
    try:
        sniff(iface=selected_interface, prn=packet_handler, store=0)
    except KeyboardInterrupt:
        print("Stopping sniffing...")

if __name__ == "__main__":
    main()
