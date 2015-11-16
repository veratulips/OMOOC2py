# -*- coding:utf-8 -*-

import sqlite3
con = sqlite3.connect('diary.db')
con.execute("CREATE TABLE diary (id INTEGER PRIMARY KEY, time char(100) NOT NULL, content char(100) NOT NULL)")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/03','中文可以吗？')")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/04','English works?')")
con.execute("INSERT INTO diary (time, content) VALUES ('15/11/05','What is the time now?')")
con.commit()