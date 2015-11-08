#####################
# echo server program

import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()

print 'Connected by',addr
while 1:
	data = conn.recv(1024)
	if not data: break
	conn.sendall(data)
conn.close()

#####################
# echo client program
import socket

HOST = 'daring.cwi.nl' # The remote HOST
PORT = 50007 # The same port as used by the server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

#
# 