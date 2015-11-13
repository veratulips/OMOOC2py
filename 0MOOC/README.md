## Python环境设置和学习资料汇总


## Mac环境设置及软件安装



## Win环境设置及软件安装

* 设置python路径

	安装后需要配置路径，参考了这篇图说位置的[教程](http://jingyan.baidu.com/article/d5a880eb6aca7213f047cc6c.html)，和这篇文字说明的[教程](http://blog.sina.com.cn/s/blog_63597aa50100iycp.html)重点如下：

	现在我假设你的python安装在C:\Python26目录下，设置环境变量方法如下：
    
    	我的电脑->属性->高级->环境变量->系统变量
    
    	在系统变量里找到PATH，双击PATH，在结尾加上 ";C:\Python26"(不要引号)
    
    	在系统变量里找到PATHEXT, 在结尾加上 ".PY;.PYM" 


* 安装pip

    在C:\Python27\Scripts目录下，cmd命令：```easy_install.exe pip```，安装成功后，cmd输入```pip```，查看。


* 配置 git & github

	首先下载[mysysgit](https://git-for-windows.github.io/)，即windows上的git安装包，然后点击安装，我是win7，安装的是```Git-2.6.3-64-bit.exe```。

	窗口界面安装中：
　
	* 在Select Components中，要选择最后一项：Use a TrueType font in all console windows (not only for Git Bash).

	* 在Select Start Menu Folder中，选择Don't create a start menu folder. 

	其他选项都是默认就好。

	然后在你习惯的工作目录里建个git的文件夹，方便以后工作。

	右键你的新建git文件夹，选择Git Bash Here，然后shell命令行就会弹出l来了。

	（操作的时候我并没有理解这个git bash是啥，弹出个shell和cmd有啥区别。）

	### 下面要做的是链接你的github并授权。

	首先你要有[github](http://github.com)帐号，没有先去注册。

	其次，你是第一次配置git，如果不是最好需要清密（详见本版块最后）。

	生成ssh密匙：

	```$ ssh-keygen -C -t rsa "your email address"```

	命令行会询问你要文件存在哪儿，密码啥的，都直接回车就好了，因为是本人本地使用。

	密匙存在默认文件夹里，我的电脑里是：C:\Users\dell\.ssh, 目标文件是：id_rsa.pub文件，打开后，复制粘贴到你的github帐号settings->SSH keys->Add SSH key->Key里。

	然后回到git bash cmd：

	```$ ssh -T git@github.com``` # 链接github

	显示中有你的github用户名就成功了，不用管它说什么：but github does not provide shell access.（虽然我很好奇吧，然而并没有跑偏去查）

	下面链接上你的用户名和邮箱

	```$ git config --global user.name "your name"```
	
	```$ git config --global user.email "your email"```

	然后是设置token

	```$ git config --global github.user yourname```
	
	```$ git config --global github.token %^&@*124976y(your token)``` # 这个在settings->personal access token，如果没有，生成一个
	
	清密：

    ```$ cd ~/. ssh```

    ```$ mkdir key_backup```

    ```$ cp id_rsa* key_backup```

    ```$ rm id_rsa*```


## Sublime上设置markdown高亮和即时预览

主要参考[Alan Lai的教程](https://wzzlj.gitbooks.io/wzzljomooc2py/content/Begin/peizhi_sublime_markdown.html)，需要注意的是Lai同学的教程是基于sublime text 3的，我的是text 2，所以在安装的时候ctrl+~后的代码在[官网](https://packagecontrol.io/installation#st2)上复制粘贴。

另外注意，修改配置要在一个md文件下才能修改



## 推荐书籍：

（1）入门三本： 

* [笨办法学Python]() ([豆瓣条目](http://book.douban.com/subject/26264642/))
* [A byte of Python(English version)](http://www.swaroopch.com/notes/python/) ([中译本豆瓣条目](http://book.douban.com/subject/5948760/))
* [Think Python](http://www.greenteapress.com/thinkpython/thinkpython.pdf) ([豆瓣条目](http://book.douban.com/subject/10779534/))

（2）进阶三本：
* Fluent Python ([豆瓣条目](http://book.douban.com/subject/26278021/))
* Python Essential Reference ([豆瓣条目](http://book.douban.com/subject/3273420/))
* Python Essential Reference 3rd edition develop's library ([豆瓣条目](http://book.douban.com/subject/1758560/))