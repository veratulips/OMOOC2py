# todo-list emample 

import sqlite3 # SQL package
from bottle import route, run, debug, template

@route('/todo') # create a route named todo 
def todo_list(): # define the todo function 
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
	result = c.fetchall()
	c.close()
	output = template('make_table',rows=result) # assign result to DB rows
	return output # this returns a page with template
	# return value would show on webpage
	# return str(result) # this returns a string


debug(True) # for developing use
run(reloader=True) # auto reloading

