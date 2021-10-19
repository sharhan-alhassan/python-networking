
# This add_client.py script

import socket

host = socket.gethostname()
port = 8097

s = socket.socket()
s.connect((host, port))

a = input('Enter first number: ')
b = input('Enter second number: ')
c = a + ', ' + b                                    # Generate string from numbers

print('Sending string {} to sever for processing...'.format(c))

s.sendall(c.encode('utf-8'))              # Converst string to bytes for transmission
data = s.recv(1024).decode('utf-8')       # Receive server response (addition results) and convert from bystes to string
print(data)                               # Convert 'string' data to 'int'

s.close()                                # close connection