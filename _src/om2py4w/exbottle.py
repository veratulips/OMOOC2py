from bottle import route, run
@route('/hello/:name')

def index(name='World'):
	return '<strong>Hello {}!'.format(name)

run(host='localhost',port=8080)
