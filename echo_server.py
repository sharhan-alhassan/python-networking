
import socket

host = socket.gethostname()
port = 8090

s = socket.socket()             # TCP socket object
s.bind((host, port))
s.listen(5)

print('Waiting for client...')
conn, addr = s.accept()         # Accept connection when client connects
print('Connected by: ', addr)

while True:
    data = conn.recv(1024)      # Receive client Data
    if not data:                # Exit from loop if no data
        break
    conn.sendall(data)          # Send the received data back to client

conn.close()                    # Close connection(You would not do this in real life as remote servers are online 24/7)

