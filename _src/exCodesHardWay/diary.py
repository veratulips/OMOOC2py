# -*- encoding=utf-8 -*- # ?? not working

import sys
import time

def menu():
	print "欢迎来到你的日志"
	print "基本功能如下："
	print "读取（r）"
	print "写入（w）"
	print "退出（q）"
	operation = raw_input("请选择您想做的事情（输入大写字母即可）：> ")
	return operation

def read():
	print "程序将读取您以往的日记"
	diary = open('diary.txt','r') 
	print diary.read()
	diary.close()
	menu()

def write():
	print "您可以开始写日记了"
	print "回车可换行输入。退出请在新一行输入：Q"
	diary = open('diary.txt','a')
	while True:
		written = raw_input('> ')
		if written == 'q':
			sys.exit()
		else:
			tmp = time.asctime()
			diary.write('\n' + tmp + ': ' + written + '\n')

diary = open('diary.txt','r') 
print diary.read()
diary.close()
operation = menu()
if operation == 'r':
	read()
elif operation == 'w':
	write()
elif operation == 'q':
	sys.exit()
