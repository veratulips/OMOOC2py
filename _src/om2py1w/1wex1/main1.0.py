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

def write(diary):
	print "您可以开始写日记了"
	diary = open('diary.txt','r')
	line = raw_input(prompt)
	diary.write(line)

def Funs():
	fun = raw_input（"""
	是否需要进行其他操作？
	读取（r）
	撰写（w）
	保存（s）
	退出（q）
	"""）
	if fun == 'r':
		read()
		elif fun == 'w'
		write()
		elif fun == 's'
		save()
		elif fun == 'q'
		close


def close():
	diary.close()

def save():
	diary.write(line)

if operation == 'read':
	read()
	otherFuns()
	close()

elif operation == 'write':
	write()
	close()
