# _*_ coding:UTF-8 _*_
from Tkinter import *

class Application(Frame):
    # 笨办法看到最后讲class部分要求如此，但是其实不太明白
    # Q1：希望能讲讲class
    def hello(self):
        print "Hello, World!"

    def createWidgets(self): # Widgets顾名思义就是小工具啦
        self.QUIT = Button(self) # 应该是设置退出按钮
        self.QUIT["text"] = "QUIT" # 按钮显示的文字
        self.QUIT["fg"] = "red" # ？的颜色
        self.QUIT["command"] = self.quit # ?

        self.QUIT.pack({"side":"left"})
        # 定义按钮组件的位置，在左边
        # pack是内嵌模块，用来定义一些列性质

        self.h = Button(self)
        self.h["text"] = "Hello"
        self.h["command"] = self.hello

        self.h.pack({"side":"left"})

    def __init__(self,master=None):
    # 尽管1W大妈讲了这个，但是似乎还是不太懂，
    # 可能是这个逻辑比较新，需要多角度反复了解几遍，才能内化
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop() # 搞了半天事没加（）导致gui不能popout啊！
root.destroy()
