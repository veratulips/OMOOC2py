# todo-list emample 

import sqlite3 # SQL package
from bottle import route, run, debug

@route('/todo') # create a route named todo 
def todo_list(): # define the todo function 
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	return str(result) # return value would show on webpage

debug(True) # for developing use
run(reloader=True) # auto reloading

