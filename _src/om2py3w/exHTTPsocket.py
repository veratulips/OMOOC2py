# an HTTP request

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connent(('yourlink',80)) # 80 is the HTTP port; yourlink ex: www.py4inf.com

# this is the thing talked in Video 2
# telnet www.XXX.com 80
# GET http://www.XXX.com/page1.htm HTTP/1.0
# then you will get connent to the website
mysock.send('GET http://yourlink/document HTTP/1.0\n\n')

# receive the info and print it out
while TRUE:
	data = mysock.recv(512) 
	if (len(data) < 1)
		break
	print data
mysock.close()

