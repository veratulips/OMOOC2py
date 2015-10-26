# -*- coding=utf-8 -*- 

from sys import argv

script, operation = argv # main.py, read, write 
prompt = '> '

def read():
	print "程序将读取您以往的日记"
	diary = open('diary.txt','r')
	# if 是否为空，
	# 	print "您的日记还没有内容。"
	# else： 
	print diary.read()

def write():
	print "您可以开始写日记了"
	diary = open('diary.txt','a')
	line = raw_input(prompt)
	save = raw_input('是否保存？保存（y）/不保存（n）')
	if save == 'y':
		diary.write('\n' + line + '\n')
		diary.close()
		print "已保存。"
	else: 
		print "未保存。"
		diary.close()


if operation == 'read':
	read()
elif operation == 'write':
	write()
