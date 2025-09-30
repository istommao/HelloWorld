import os
import socket
import struct
import dpkt

# Create a raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Create an ICMP Echo Request packet
icmp = dpkt.icmp.ICMP.Echo()
icmp.id = os.getpid() & 0xFFFF  # Use process ID as ICMP ID
icmp.seq = 1  # Sequence number
icmp.data = b'Hello, World!'  # Payload data

# Create an ICMP packet and add Echo Request
icmp_pack = dpkt.icmp.ICMP()
icmp_pack.type = dpkt.icmp.ICMP_ECHO
icmp_pack.data = icmp

# Create an IP packet and add ICMP packet
ip = dpkt.ip.IP()
ip.src = socket.inet_aton('192.168.1.5')  # Source IP address
ip.dst = socket.inet_aton('192.168.1.11')  # Destination IP address
ip.p = socket.IPPROTO_ICMP  # Protocol type
ip.data = icmp_pack

# Send IP packet
s.sendto(bytes(ip), ('192.168.1.11', 0))

# Receive response
while True:
    data, addr = s.recvfrom(1024)
    print(addr)
    if addr[0] == '192.168.1.11':  # If response comes from the host we pinged
        ip_resp = dpkt.ip.IP(data)
        icmp_resp = ip_resp.data
        if icmp_resp.type == dpkt.icmp.ICMP_ECHOREPLY:  # If it's an ICMP Echo Reply
            print(f'Received ICMP Echo Reply: ID={icmp_resp.data.id}, Seq={icmp_resp.data.seq}, Data={icmp_resp.data.data}')
            break
