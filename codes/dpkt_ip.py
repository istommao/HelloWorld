import socket
import dpkt

# create raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# create ip package
ip = dpkt.ip.IP()
ip.src = socket.inet_aton('192.168.1.5')
ip.dst = socket.inet_aton('192.168.1.11')
ip.p = socket.IPPROTO_TCP

# create tcp package
tcp_pkg = dpkt.tcp.TCP()
tcp_pkg.sport = 12345
tcp_pkg.dport = 80
tcp_pkg.flags = dpkt.tcp.TH_SYN

ip.data = tcp_pkg

# send ip package
s.sendto(bytes(ip), ('192.168.1.11', 0))
