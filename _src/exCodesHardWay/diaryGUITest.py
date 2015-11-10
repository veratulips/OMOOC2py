# -*- coding=UTF-8 -*- # 

from Tkinter import *
# from diary import *

import sys 
reload(sys)
sys.setdefaultencoding('utf8') # learning from wzzlj

class Application(Frame):
	def read(self):
		diary = open('diary.txt','r') 
		print diary.read()

	def write(self):
		print "您可以开始写日记了"
		diary = open('diary.txt','a+')
		written = raw_input('> ')
		tmp = time.asctime()
		diary.write('\n' + tmp + ': ' + written + '\n')

	# def save(self):


	def createWidgets(self):
		# new input
		
		self.label = Label(self,text="请输入您的日记：")
		# self.label.grid()

		# define entry properties
		self.input = StringVar(self)
		self.entry = Entry(self.textvariable=self.input) # need width
		self.entry.cat = ("<Return>", self.write) # 回车后写入日记
		# self.entry.grid()

		# # save button
		# self.SAVE = Button(self) 
		# self.SAVE["text"] = "SAVE" 
		# self.SAVE["fg"] = "red" 
		# self.SAVE["command"] = self.save 

		# quit button
		self.QUIT = Button(self) 
		self.QUIT["text"] = "QUIT" 
		self.QUIT["fg"] = "red" 
		self.QUIT["command"] = self.quit 


	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets() 

		
root = Tk()
root.title('My Diary App')
app = Application(master=root)
app.mainloop()