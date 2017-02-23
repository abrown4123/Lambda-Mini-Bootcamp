from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Open database successfully')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created successfully')
connection.close()


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/new')
def new_post():
	return render_template('new.html')
	
@app.route('/addrecord', methods = ['POST'])
def addrecord():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	
	try:
		title = request.form['title']
		post = request.form['post']
		cursor.execute('INSERT INTO posts (title,post) VALUES (?,?)', (title,post))
		connection.commit()
		message = 'Record successfully added'
	except:
		connection.rollback()
		message = 'error in insert operation'
	finally:
		return render_template('result.html', message = message)
		connection.close()
	