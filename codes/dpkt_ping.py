import os
import socket
import struct
import dpkt

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

def create_ip_pkg(src, dst, data):
    ip = dpkt.ip.IP()
    ip.src = socket.inet_aton(src)
    ip.dst = socket.inet_aton(dst)
    ip.p = socket.IPPROTO_ICMP
    ip.data = data

    return ip


def create_icmp_pkg():
    icmp = dpkt.icmp.ICMP.Echo()
    icmp.id = os.getpid() & 0xFFFF  # 使用进程 ID 作为 ICMP ID
    icmp.seq = 1  # 序列号
    icmp.data = b'Hello, World!'

    # 创建一个 ICMP 包并添加 Echo Request
    icmp_pack = dpkt.icmp.ICMP()
    icmp_pack.type = dpkt.icmp.ICMP_ECHO
    icmp_pack.data = icmp
    return icmp_pack


data = create_icmp_pkg()
ip = create_ip_pkg("192.168.1.15", "192.168.1.11", data)
resp = s.sendto(bytes(ip), ('192.168.1.11', 0))
print(resp)




# # 创建一个 ICMP Echo Request 包
# icmp = dpkt.icmp.ICMP.Echo()
# icmp.id = os.getpid() & 0xFFFF  # 使用进程 ID 作为 ICMP ID
# icmp.seq = 1  # 序列号
# icmp.data = b'Hello, World!'  # 载荷数据

# # 创建一个 ICMP 包并添加 Echo Request
# icmp_pack = dpkt.icmp.ICMP()
# icmp_pack.type = dpkt.icmp.ICMP_ECHO
# icmp_pack.data = icmp

# # 创建一个 IP 包并添加 ICMP 包
# ip = dpkt.ip.IP()
# ip.src = socket.inet_aton('192.168.1.5')  # 源 IP 地址
# ip.dst = socket.inet_aton('192.168.1.11')  # 目标 IP 地址
# ip.p = socket.IPPROTO_ICMP  # 协议类型
# ip.data = icmp_pack

# # 发送 IP 包
# resp = s.sendto(bytes(ip), ('192.168.1.11', 0))
# print(resp)

