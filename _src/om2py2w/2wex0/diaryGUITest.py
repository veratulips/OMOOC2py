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
		diary = open('diary.txt','a')
		written = self.entry.get() # .get can get the text
		self.entry.delete(0,END) # clear the text column
		diary.write('\n' + written)
		diary.close()

	def createWidgets(self):
		# new input
		
		self.label = Label(self,text="请输入您的日记：").pack(side=LEFT)
		# self.label.grid()

		# define entry properties
		self.input = StringVar(self)
		self.entry = Entry(self,textvariable=self.input).pack(side=LEFT) # need width
		

		# read button
		self.READ = Button(self) 
		self.READ["text"] = "读取" 
		self.READ["fg"] = "red" 
		self.READ["command"] = self.read
		self.READ.pack(side=LEFT)

		# save button
		self.SAVE = Button(self) 
		self.SAVE["text"] = "保存" 
		self.SAVE["fg"] = "red" 
		self.SAVE["command"] = self.write # ? 
		self.SAVE.pack(side=LEFT)

		# quit button
		self.QUIT = Button(self) 
		self.QUIT["text"] = "退出" 
		self.QUIT["fg"] = "red" 
		self.QUIT["command"] = self.quit 
		self.QUIT.pack(side=RIGHT)


	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets() 

		
root = Tk()
root.title('My Diary App')
app = Application(master=root)
app.mainloop()
