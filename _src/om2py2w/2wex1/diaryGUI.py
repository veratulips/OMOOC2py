# -*- coding=UTF-8 -*- # 

from Tkinter import *
# from diary import *

import sys 
reload(sys)
sys.setdefaultencoding('utf8') # learning from wzzlj 还是不能输入中文？

class Application(Frame):
	def read(self): #? 
		diary = open('diary.txt','r')
		self.txt = Text(self,width=51,height=20) # size changeable
		# self.txt.config(state=NORMAL)
		self.txt.insert(END,diary.read())
		self.txt.see(END)
		# self.txt.config(state=DISABLED)

	def write(self,written): # 写了written就对了。为什么？
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
		self.entry = Entry(self)
		self.entry.bind("<Return>",self.write)
		self.entry.pack(side=LEFT) # need width

		# read button
		self.READ = Button(self) 
		self.READ["text"] = "读取" 
		self.READ["fg"] = "red" 
		self.READ["command"] = self.read
		self.READ.pack(side=LEFT)

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
# root.geometry('400x420+400+400')
root.title('My Diary App')
app = Application(master=root)
app.mainloop()
