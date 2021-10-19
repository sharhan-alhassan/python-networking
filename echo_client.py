

import socket

host = socket.gethostname()
port = 8090

s = socket.socket()                         # TCP socket objec

s.connect((host, port))
s.sendall(b'This will be sent to server!')  # Send this message to server

data = s.recv(1024)                         # Now, receive the echoed data from server

print(data)                                 # Print received(echoed) data
s.close()