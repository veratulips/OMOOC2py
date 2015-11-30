import sae
from bottle import Bottle, run

app = Bottle()

@app.route('/')
def hello():
	return "Hello, world! - Bottle"

application = sae.create_wsgi_app(app)