import os
import socket
import struct
import dpkt

# 创建一个原始套接字
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# 创建一个 ICMP Echo Request 包
icmp = dpkt.icmp.ICMP.Echo()
icmp.id = os.getpid() & 0xFFFF  # 使用进程 ID 作为 ICMP ID
icmp.seq = 1  # 序列号
icmp.data = b'Hello, World!'  # 载荷数据

# 创建一个 ICMP 包并添加 Echo Request
icmp_pack = dpkt.icmp.ICMP()
icmp_pack.type = dpkt.icmp.ICMP_ECHO
icmp_pack.data = icmp

# 创建一个 IP 包并添加 ICMP 包
ip = dpkt.ip.IP()
ip.src = socket.inet_aton('192.168.1.5')  # 源 IP 地址
ip.dst = socket.inet_aton('192.168.1.11')  # 目标 IP 地址
ip.p = socket.IPPROTO_ICMP  # 协议类型
ip.data = icmp_pack

# 发送 IP 包
s.sendto(bytes(ip), ('192.168.1.11', 0))

# 接收响应
while True:
    data, addr = s.recvfrom(1024)
    print(addr)
    if addr[0] == '192.168.1.11':  # 如果响应来自我们 ping 的主机
        ip_resp = dpkt.ip.IP(data)
        icmp_resp = ip_resp.data
        if icmp_resp.type == dpkt.icmp.ICMP_ECHOREPLY:  # 如果是 ICMP Echo Reply
            print(f'Received ICMP Echo Reply: ID={icmp_resp.data.id}, Seq={icmp_resp.data.seq}, Data={icmp_resp.data.data}')
            break
