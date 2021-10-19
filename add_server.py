
# This is add_server.py script

import socket 

host = socket.gethostname()
port = 8097

s = socket.socket()
s.bind((host, port))
s.listen(5)

print('Waiting for connection...')
conn, addr = s.accept()

while True:
    data = conn.recv(1024)                     # Receive data in bytes
    decoded_data = data.decode('utf-8')        # Decode data from bystes to string
    d = decoded_data.split(",")                # Split the received string using ',' as separator and store in list 'd'
    add_data = str(int(d[0]) + int(d[1]))      # add the content after converting to 'int'
    conn.sendall(add_data.encode('utf-8'))     # Stringify results and convert to bytes for transmission (String conversion is a must)

conn.close()                     
