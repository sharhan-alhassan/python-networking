
# This is udp_client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 8888

msg = b"Hello, Python"
print("UDP Target IP: ", udp_host)
print("UDP Target Port: ", udp_port)

s.sendto(msg, (udp_host, udp_port))