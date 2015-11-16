# -*- coding:utf-8 -*-

from bottle import route, run, template, request
import sqlite3
import os
from datetime import datetime

filename = 'diary.txt'

if not os.path.exists(filename):
    f = open(filename,'w')
    f.close()

webpage = '''
<html>
<head>
    <title> Diary-web </title>
</head>
<body>
    <p>请输入日记内容:</p>
    <form action="/diary" method="POST">
        <input type="text" size="100" maxlength="100" name="filename">
        <input type="submit" name="save" value="save">
    </form>
    <ul>
        {{input}}
    </ul>
</body>
</html>
'''

@route('/diary')
def readDiary():
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("SELECT content FROM diary")
    result = c.fetchall()
    conn.commit()
    c.close()
    f = open(filename,'r')
    content = f.read()
    # print content 
    f.close()
    return template(webpage,input=content) # aim: print out the diary 

@route('/diary',method='POST')
def writeDiary():
    line = request.POST.get('line','')
    
    if line:
        time = datetime.now()
        t = time.strftime("%y/%m/%d")
        f = open(filename,'a')
        update = t + '\t' + line + '\n'
        f.write(update)
        content = f.read()+'\n'+update
        # print content
        f.close()

    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("INSERT INTO diary (time,content) VALUES (?,?)",(t,new))
    result = c.fetchall()
    conn.commit()
    c.close()
    return template(webpage,input=content)




run(host = 'localhost', port = 8080, debug=True)
