# -*- coding:utf-8 -*-

import requests 

print '''
日记基本功能：
读取（r）
退出（q）
如需写入，请在 > 后键入内容
'''

# 将用户input传进server

def postdata(data):
	r = requests.post('http://localhost:8080/diary',data={'content':data})

# 从服务器读取日记
def readdiary():
	r = requests.get('http://localhost:8080/diary')
	return r.content

while True:
	data = raw_input("请输入日记内容 >")
	if data == 'q':
		print "已退出"
		break
	elif data == 'r':
		print readdiary()
	else:
		postdata(data)