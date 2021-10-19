
# tcp_server.py script
'''
We defined TCP socket by merely writing S=socket.socket(), that is without providing the socket_family and the socket_type. If we do not mention the socket_family and socket_type, then by default it is TCP. So, if we want to create a UDP socket than we have to specify socket_family and socket_type explicitly.
'''

import socket
s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host, port))

print("Waiting for connection...")
'''
We bind the socket to the given port on our local machine. In the listening stage, we make sure we listen to multiple clients in a queue using the backlog argument to the listen() method.
'''
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got connection from ', addr)
    conn.send(b'Server Saying Hi')
    conn.close()