from Tkinter import *

class Application(Frame): 
	def hello(self):
		print "Hello, World!"

	def createWidgets(self): 
		self.QUIT = Button(self) 
		self.QUIT["text"] = "QUIT" 
		self.QUIT["fg"] = "red" 
		self.QUIT["command"] = self.quit 

		self.QUIT.pack({"side":"left"}) 

		self.h = Button(self)
		self.h["text"] = "Hello"
		self.h["command"] = self.hello

		self.h.pack({"side":"left"})

	def __init__(self,master=None): 
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
