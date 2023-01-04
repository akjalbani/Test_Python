'''
This code captures packets from the eth0 interface, filters out non-TCP packets, 
and keeps track of the number of packets and bytes received from each IP address. 
If the packet count or byte count for any IP address exceeds the specified threshold, 
the code prints a message indicating that a possible DDoS attack has been detected. 
The captured packets are also written to a pcap file for later analysis.

'''

import pcapy
import sys

# Open a file to write the captured packets to
pcap_file = open("captured_packets.pcap", "w")

# Create a pcapy writer object
writer = pcapy.PcapWriter(pcap_file, linktype=pcapy.DLT_EN10MB)

# Set up a packet capture filter to capture only TCP packets
filter = "tcp"

# Create a pcapy capture object
capture = pcapy.open_live("eth0", 65536, True, 1000)
capture.setfilter(filter)

# Set up variables to keep track of the number of packets and bytes
# received from each IP address
ip_counts = {}
ip_bytes = {}

# Set the threshold for the number of packets and bytes that will trigger
# an alert for a DDoS attack
packet_threshold = 1000
byte_threshold = 1000000

# Start the capture loop
while True:
    # Capture a single packet
    (header, packet) = capture.next()

    # Extract the source IP address from the packet
    src_ip = packet[12:16]

    # Increment the packet and byte counts for the IP address
    if src_ip in ip_counts:
        ip_counts[src_ip] += 1
        ip_bytes[src_ip] += header.getlen()
    else:
        ip_counts[src_ip] = 1
        ip_bytes[src_ip] = header.getlen()

    # Check if the packet count or byte count for any IP address has exceeded the threshold
    for src_ip, count in ip_counts.items():
        if count > packet_threshold or ip_bytes[src_ip] > byte_threshold:
            print("Possible DDoS attack detected from IP address {}!".format(src_ip))

    # Write the packet to the pcap file
    writer.writepkt(packet, header)

# Close the pcap file
pcap_file.close()
