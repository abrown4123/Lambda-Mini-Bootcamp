from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('home.html')
	
@app.route('/birthday')
def birthday():
	return "October 30 1911"

@app.route('/birthday/<name>')
def hello(name):
	return "Hello " + name + '!'

@app.route('/sum/<int:a>/<int:b>')
def add(a, b):
	total =  a + b;
	return str(total)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
	total =  a * b;
	return str(total)
	
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
	total =  a - b;
	return str(total)	
	
@app.route('/favoritefoods')
def list():
	foods = ['pizza', 'ice cream', 'peanut butter']
	return jsonify(foods)