
#!usr/bin/python3

import socket

s = socket.socket()
host = socket.gethostname()
port = 8010

s.connect((host, port))
s.setblocking(1)
# Or simply omit this line as by default TCP sockets
# are in blocking mode

data = "Hello Python\n" *10*1024*1024       # Huge amount of data to be sent
assert s.send(data.encode('utf-8'))                         # Send data till true