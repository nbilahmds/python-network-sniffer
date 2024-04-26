from scapy.all import *
from prettytable import PrettyTable

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

# Sniff network traffic
print("Sniffing network traffic... (Ctrl+C to stop)")
try:
    sniff(prn=packet_handler, store=0)
except KeyboardInterrupt:
    print("Stopping sniffing...")
