
#!usr/bin/python3

import socket

t_host = input('Enter the host to be scanned: ')        # Target host: eg; www.cloudbintech.com
t_ip = socket.gethostbyname(t_host)                     # Resolve host(dns name) to IPv4

print('Your IP Address is: ', t_ip)

while 1:
    t_port = int(input('Enter port to be scanned: '))   # Port number

    try:
        s = socket.socket()
        response = s.connect((t_ip, t_port))
        print('Port {} status: Open'.format(t_port))
    except :
        print('Port {} status: Closed'.format(t_port))

print('Porting scanning complete!')
