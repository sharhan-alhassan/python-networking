

# This is a udp_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_host = socket.gethostname()
udp_port = 8888

s.bind((udp_host, udp_port))

while True:
    print('Waiting for client...')
    data, addr = s.recvfrom(1024)
    print('Received Messages:', data, ' from ', addr)