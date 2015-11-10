# -*- coding=UTF-8 -*- # 

from Tkinter import *
import diary

import sys 
reload(sys)
sys.setdefaultencoding('utf8') # learning from wzzlj

class Application(Frame):
	def createWidgets(self):
		# label
		self.label.pack({"sdie":"left"})
		self.label = Label(self,text='input: ',font=("Arial",20))

		# entry
		self.entry.pack({"side":"left"})
		self.entry = Entry(self,textvariable=self.line,fg='black',bg='grey',font=("Arial",20,"normal"),width=43)

		# button
		self.button.pack({"side":"left"})
		self.button = Button(self,text='exit',font=("Arial",20))
		self.button['command']=self.quit

		self.text.pack()
		self.text = Text(self,bg='grey', font=("Arial", 18), width='60', height='20')
		lines = read(file)
		for line in lines:
			self.text.insert(END,line)

		self.text.congif(start=DISABLED)
		self.text.see(END)

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets() 

		
def diaryGUI():
	root = Tk()
	root.title('My Diary App')
	app = Application(master=root)
	app.mainloop()

if __name__ == "__diaryGUI__":
	diaryGUI()