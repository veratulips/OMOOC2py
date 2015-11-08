# -*- coding:utf8 -*- 

import socket 
import os
# 建立协议，当client发送退出信号，返回日记历史信息

quitwd = 'q'

def response(s,data,addr):
    if data == 'q':
        f = open('diary.txt')
        msg = f.read()
        f.close()
        print msg
        s.sendto(msg,addr)
        print 'send back to',addr,'and quit'
    else:
        f = open('diary.txt', 'a')
        f.write(data + '\n')
        print data
        f.close()

def main():
    if not os.path.exists('diary.txt'):
        f=open('diary.txt','w')
        f.close()

    port = 10000  # 数字是默认的吗？
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #从指定的端口，从任何发送者，接收UDP数据
    s.bind(('localhost',port))

    print('正在等待接入...')
    
    while True:
    #接收一个数据
        print "\n已接入，正在等待信息"
        data,addr=s.recvfrom(1024)
        print 'Received:',data,'from',addr
        response(s,data,addr)


    s.close()

if __name__ == '__main__':
    main()