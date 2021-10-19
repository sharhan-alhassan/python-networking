
import socket
from pprint import pprint
'''
Banner Grabbling to know what services and their
versions eg: (nginx, mysql, ftp) are running in a 
particular port
'''
s = socket.socket()

t_host = input('Enter host name: ')
t_port = input('Enter host name: ')

s.connect((t_host, int(t_port)))

s.sendall('GET HTTP/1.1 \r\n'.encode('utf-8'))

ret = s.recv(1024)

pprint('[+] ' + str(ret))