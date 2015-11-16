#4W-学习笔记

###**过程流水帐**

[20151109] Google了一下[bottle](http://bottlepy.org/docs/dev/index.html)和[Jinja2](http://jinja.pocoo.org/docs/dev/)的官方文档，准确地说应该是开发者网站。读了一些基本内容，安装好了。

安装 bottle：

* ```pip install bottle```

安装 Jinja2:

* ```pip install Jinja2```

如果出现如下报错：

```Requirement already satisfied (use --upgrade to upgrade): MarkupSafe in/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages (from Jinja2)```

应该是已经安装配置好了吧，或者更新一下，以防万一。

```pip install Jinja2 --upgrade```

之后显示的是：

```Requirement already up-to-date: Jinja2 in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages```

这些应该没问题了。

明天上班空闲去读文档。

[20151110-1111] 因为上周补python，没有看FRM Notes。这两天补了FRM Notes，就没有看python。

[20151112] 今天把4w作业的框架写了一下，但是这周工作的任务特别多，所以在工作时间基本上看不了代码写不了啥。上周的视频还没有看，今天晚上补上。

几个基本功能：

* route()
* run()
* template()

待阅读实现的功能：

* [request](http://docs.python-requests.org/en/latest/user/quickstart/)

* [html代码格式](http://docs.python-guide.org/en/latest/scenarios/scrape/)

* [备选教程](http://gotofritz.net/blog/weekly-challenge/restful-python-api-bottle/)

[20151114] 前面的任务断开了，今天决定从官网的[todo－list的例子](http://bottlepy.org/docs/dev/tutorial_app.html)做一下，因为基本功能模块都有涉及。

* 建立SQL database: ```import sqlite3```

* route() route of bottle: a certain address on the server. 
  
	dynamic routes: ```@route('/myroute/<sth>')```
	"The key point here is the colon. This tells Bottle to accept for :something any string up to the next slash. Furthermore, the value of something will be passed to the function assigned to that route, so the data can be processed within the function."

	dynamic routes using regular expressions: ```@route(/item<item_:re:[0-9]+>)```

* run() starts the web server included in Bottle

* return what you want to see in the browser

* debug() & run(reloader=True)

* templates are stored as separae files having a ```.tpl``` extension, which uses HTML-markup mixed with Python statement. 

	template formatting: % is interpreted as Python code; others are plain HTML markup.

	If you need to access a variable within a non-Python code line inside the template, you need to put it into double curly braces. This tells the template to insert the actual value of the variable right in place.

* GET & POST of ```request``` 

####Trouble shooting process: 

1. error msg: ```error: [Errno 48] Address already in use```

	google results [1](http://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use) [2](http://stackoverflow.com/questions/7703797/need-to-close-python-socket-find-the-current-running-server-on-my-dev-environm): it seems that socket is not closed but I tried this two ways, it is not work. and I tried ```ps -fA | grep python``` there is no ongoing process, except ```502  3243  1743   0 10:06AM ttys000    0:00.00 grep python```, and I tried ```kill 3243```, it says ```-bash: kill: (3243) - No such process```. 

	I am going to try restart the browser and terminal. When I am going to quit the terminal it says that my Python is running there, so this is probably the problem. But it seems I didn't know how to kill that. 

	Then I googled search kw: bottle + error msg:

	I got this [page](http://stackoverflow.com/questions/17044939/python-bottle-can-run-two-programs-on-the-same-address-and-port-on-windows), though this is not directly the same as my situation but when I saw the ```run(host='localhost',port=9999)```, I realized that the parameters in run() matters, thus, I changed the ```run(reloader=True)``` back to ```run()```, everything worked. 


2. error msg: ```Error: 500 Internal Server Error```

3. [coding problems illustration](https://www.python.org/dev/peps/pep-0263/): I happend to find this page. 

4. How can I know whether the data is saved in database? [Similar questions on stackoverflow](http://stackoverflow.com/questions/2440147/how-to-check-the-existence-of-a-row-in-sqlite-with-python), needs more reading and tries on this. 

####Pickups:

[a quick start about sqlite3 of database](http://pythontips.com/2013/08/01/connecting-to-sqlite-databases/).

[pythontips](http://pythontips.com/python-resources/): a good website for searching and learning. However, I actually don't have time to read more. 

Q&A: 

1. what is tuple? 

2. How can I view data in database(*.db)? 

---

###感想 

上班的时候时间都是零碎的，编程这种任务，由于是新手，所以需要很多时间和精力，需要沉浸，所以上班的时候基本上写不了什么代码，而且效率不高。本周实验发现，可以看一些短小的知识点，但是这个就需要头一天晚上分割好知识点和任务，初步查好内容。

周末是比较好的编程的时间，以后要更好利用。目前的问题是周末还想休息一下，这个tradeoff就比较麻烦了。

最后就是，最近的确要学的内容有些多，平常还要看FRM看书，所以平衡起来比较辛苦。

本周基本上就是之前安排的社交活动基本完结，到年底前，决定不再安排了，集中精力学习这些内容和睡觉。

今年实在是太累太辛苦了，但是很开心。2015-11-12
