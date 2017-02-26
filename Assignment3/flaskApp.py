from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')
	
@app.route('/enternew')
def enterfood():
	return render_template('food.html')
	
@app.route('/addfood', methods = ['POST'])
def addfood():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	
	try:
		name = request.form['name']
		calories = request.form['calories']
		cuisine = request.form['cuisine']
		vegetarian = request.form['is_vegetarian']
		gluten = request.form['is_gluten_free']
		cursor.execute('INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)', (name,calories,cuisine,vegetarian,gluten))
		connection.commit()
		message = 'Record successfully added'
	except:
		connection.rollback()
		message = 'error in insert operation'
	finally:
		return render_template('result.html', message = message)
		connection.close()
		
@app.route('/favorite')
def favorite():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	
	try:
		cursor.execute('SELECT * FROM foods WHERE name = "peanut butter"')
		connection.commit()
		favorite = cursor.fetchone()
		
	except:
		favorite = "Did you forget to add Peanut Butter?"
	
	finally:
		return jsonify(favorite)
		connection.close()
	
@app.route('/search')
def search():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	
	try:
		name = (request.args.get('name'),)
		cursor.execute('SELECT * FROM foods WHERE name =?', name)
		connection.commit()
		search = cursor.fetchone()
		
	except: 
		search = "try again"
		
	finally:
		return jsonify(search)
		connection.close()
	
@app.route('/drop')
def drop():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	
	try:
		cursor.execute('DROP TABLE foods')
		connection.commit()
		drop = "Dropped"
	
	except:
		drop = 'Something went wrong'
	
	finally:
		return drop
	
	
	
	
	
	
		
	
	
	
	
	
	