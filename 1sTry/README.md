# 笨办法学Python

以下笔记按习题顺序，无整体逻辑，只摘录出自己认为需要注意的点和需要反复看的点。
其中的问题也一并记录了，不过很多都没有解决，需要独立出Q&A板块。

##习题4：变量的命名
* 出现的错误主要都是typo
* 问题：浮点数到底有啥意义？就是可以算小数点吗？

##习题5：格式化字符串 （format string）
* 问题：''是字符串；“”是？

    
    %s 字符串
    
    %d 数字
    
    %r 无论什么都打印出来

    e.g.
    name='Zed A. Shaw'
    print "Let's talk about %s." % name

* [参考](http://www.cnblogs.com/gotaly/articles/2583250.html)

    ```
    %+8.6f ---> % 转换标志 最小宽度 精度 类型
    sign: + 右对齐（default）; - 左对齐; 0 用0填充空出位置
    ```

* 其他一些格式：
```
nameAge={"zhang":10,"wang":11,"li":32} # 用到了列表
"wang's age is %(wang)d" % nameAge
```

* 更高级的方法：
```
s.format(*args, *kwargs) # 可以认为是一种函数调用
```
    但是我认为我记不住这些方式，肯定还是要遇到多了自然就知道了。
    
##习题6：字符串和文本基础
    
    print "I also said '%s'." % y # notice that '%s' = %r ~= %s
    print "I also said %s." % y
    
* 主旨是要注意数据类型```type()```
    

##习题7：复习

    print "."*10  # this is intersting
    print end1+end2+end3+end4+end5+end6, # the comma actually connects these two print
    print end7+end8+end9+end10+end11+end12

##习题9
* ```\n``` 换行
* ```print """ 
XXX
"""```可以直接输出一段话这样子

##习题11
一般软件做的事情主要就是下面几条：
1. 接受人的输入。
2. 改变输入。
3. 打印出改变了的输入。

 ```raw_input()``` 用法

##习题12

* 所以: ```raw_input("这里直接加入要输出的话")，然后后面要求用户输入```

* python -m pydoc raw_input (调用pydoc的方法)

##习题13
* 重要概念：解包（unpack）。这的确是一个很方便的概念，一个argv里面可以存很多variables

* ```import 模组(modules)```

##习题17
* 命令```exists```。
    
    *这个命令将文件名字符串作为参数,在mac上试一下 cat copied.txt
我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接
(concatenate)”到一起，不过实际上它最大的用途是打印文件内容到屏幕
上。你可以通过 man cat 命令了解到更多信息。
*

###**出差了4天，进度落下来了**

##习题23
书里提供的有大量python代码网站：

* bitbucket.org
* github.com
* launchpad.net
* koders.com

##习题25
* 运行python后，需要执行文件用```ipmort filename``` （这里是把.py文件当作一个模组来使用）
* ```ex25.break_words``` 是运行里面具体函数的方法
* ```help(ex25)``` or ```help(ex25.break_words)``` 我在win下无法执行？
* ```from ex25 import *```
* python编译器是什么？sublime是编译器吗？

##习题27 一周内完成 开始学逻辑关系
* 真值表:表四 没理解为什么 true+ture=false？后来发现应该是打印错误了。我在cmd里面输出的结果是true

##习题29&30
* 注意if语句的格式

        if XX:
            blablabla
        elif XX:
            blablabla
        else:
            blablabla  
    
* 最容易出现的问题就是不加：
  

##习题32：
    你要做的是以 [ （左方括号）开头“打开”列表，然后写下你要放入列表的东西，
    用逗号隔开，就跟函数的参数一样，最后你需要用 ] （右方括号）结束右方括号的定义

##习题33： while循环
    回到while 循环，它所作的和if语句类似，也是去检查一个布尔表达式的真假，
    不一样的是它下面的代码片段不是只被执行一次，
    而是执行完后再调回到while所在的位置，如此重复进行，
    直到 while 表达式为False 为止。
    while循环需要i=i+1的counter

##习题34
* python里的列表是从0开始算的，不是1！！！
* oridinal number 序数
* cardinal number 基数

##习题35
* 最爱犯的错就是if后面不加： 

##习题36
    这里的if语句没有end做结尾，所以需要else+die函数做结尾
    “如果这个 else 永远都不应该被执行到，因为它本身没有任何意义，那你
    必须在else 语句后面使用一个叫做die 的函数，让它打印出错误信息并且
    死给你看，这和上一节的习题类似，这样你可以找到很多的错误。”

    关于debug
    “最好的调试程序的方法是使用 print 在各个你想要检查的关键环节将关键
    变量打印出来，从而检查哪里是否有错。”
    
    看来matlab里面的debug方式太user-friendly了，
    所以我之前还找那种如何debug看到函数赋值的工具呢。”
    
    让程序一部分一部分地运行起来。不要等一个很长的脚本写完后才去运行
    它。写一点，运行一点，再修改一点“
    这一点也蛮不一样的，主要是因为debug的方式不一样
    
* 应该需要问一下python里面的debug是个啥形式的？

##习题37
待完成：主要是还是没有学会如何搜索python官方帮助文档。
找到的可以学习的相关python代码：

##习题39 
* 列表操作：append追加
* 问题：append还有split这种函数或者功能在哪里检索查到啊？
    .append .pop .join .split
* class() 类 ？看得一头雾水，不知道怎么用
    dir() 
* 应该需要返工！

##习题40
* 字典：dict (or hash)

##习题43 class

##习题46 骨架：Page 122

2015-10-29 