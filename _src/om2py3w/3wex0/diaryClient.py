# _*_ coding:utf8 _*_

import socket

quitwd = 'q'

port=10000
host='localhost'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# print 'history:'
# print data

msg = ''
while True:
	msg = raw_input('> ')
	
	if msg != '':
		s.sendto(msg,(host,port))
		msg += msg + '\n' 
		print 'messages sent'
	elif msg in ['q','quit','exit']:
		s.sendto(quitwd,(host,port))
		data, server=s.recvfrom(1024)
		print 'safely exit'
		break

s.close()
