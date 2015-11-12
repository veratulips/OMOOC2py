# -*- coding:utf-8 -*-

from bottle import route, run, template, request

from datetime import datetime
import sys

def read():

def write():

diaryWeb_tpl = '''
写网页格式 template
'''


@route('/diary')
def readDiary():
	data = read()
	return template(diaryWeb_tpl,d=data)

@route('/diary')
def writeDiary():
	request.POST.get

	return template(diaryWeb_tpl,d=data)

run(host = 'localhost', port = 8080, degug=True)

# time.strftime()
# sqlite3 数据库