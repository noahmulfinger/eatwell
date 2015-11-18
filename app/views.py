from flask import Flask, g, render_template, session, request, redirect, url_for, flash, Markup
from werkzeug import generate_password_hash, check_password_hash
from app import app, mysql, models #, login_manager

import time

import functions

#from .models import User

#from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required

# Not the best way to do this, look in to Flask-Login
global user_id
user_id = None

@app.route('/')
@app.route('/index')
# @login_required
def index():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	user_meals = functions.get_result("SELECT Food_Item.*, Eats.time \
									 FROM Food_Item, Eats \
									 WHERE Food_Item.item_id = Eats.item_id \
									 AND Eats.user_id = %s", [user_id])

	user_symptoms = functions.get_result("SELECT Symptom.*, Has.rating, Has.time \
									    FROM Symptom, Has \
									    WHERE Symptom.symptom_id = Has.symptom_id \
									    AND Has.user_id = %s", [user_id])

	return render_template('index.html',  user_meals=user_meals, user_symptoms=user_symptoms)




@app.route('/fooditem/<item_id>')
def get_item(item_id):
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	item = functions.get_result("SELECT Food_Item.* \
							   FROM Food_Item \
							   WHERE Food_Item.item_id = %s", [item_id])

	if not item:
		message = Markup('<div class="flash alert alert-danger">Food item does not exist.</div>')
		flash(message)
		return redirect(url_for('index'))

	ingredients = functions.get_result("SELECT Ingredient.* \
									  FROM Ingredient, Contains \
									  WHERE Contains.item_id = %s \
									  AND Ingredient.ingredient_id = Contains.ingredient_id",
									  [item_id])

	badges = functions.get_result("SELECT Badge.* \
								 FROM Badge, Tagged_With \
								 WHERE Tagged_With.item_id = %s \
								 AND Badge.badge_id = Tagged_With.badge_id",
								 [item_id])

	return render_template('fooditem.html', item=item, ingredients=ingredients, badges=badges)

@app.route('/newitem')
def new_item():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	return render_template('newitem.html')

@app.route('/additem', methods=['POST','GET'])
def add_item():
	input_name = request.form['input_food_item']
	input_ingr = request.form['input_ingr']

	if input_name and input_ingr:

		conn = mysql.connect()
		cursor = conn.cursor()

		# Insert item and then get its id
		statement = "INSERT INTO Food_Item (name) VALUES (%s)"
		cursor.execute(statement, [input_name])
		query = "SELECT Food_Item.item_id FROM Food_Item WHERE Food_Item.name = %s"
		cursor.execute(query, [input_name])
		data = cursor.fetchone()
		item_id = int(data[0])

		# Insert time and then get its id
		now_date = time.strftime('%Y-%m-%d')
		now_time = time.strftime('%H:%M:%S')
		statement = "INSERT INTO Time (date, time) VALUES (%s, %s)"
		cursor.execute(statement, [now_date, now_time])
		query = "SELECT Time.time_id FROM Time WHERE Time.date = %s AND Time.time = %s"
		cursor.execute(query, [now_date, now_time])
		data = cursor.fetchone()
		time_id = int(data[0])

		# Insert eats relationship using above ids and current user id
		statement = "INSERT INTO Eats (time_id, user_id, item_id) VALUES (%s, %s, %s)"
		cursor.execute(statement, [time_id, user_id, item_id])

		ingr_list = map(str.strip, str(input_ingr).split(','))
		for ingr in ingr_list:
			# Insert ingredient and get its id
			statement = "INSERT INTO Ingredient (name) VALUES (%s)"
			cursor.execute(statement, [ingr])
			query = "SELECT Ingredient.ingredient_id FROM Ingredient WHERE Ingredient.name = %s"
			cursor.execute(query, [ingr])
			data = cursor.fetchone()
			ingr_id = int(data[0])

			# Insert contains relationships using item id and ingredient ids
			statement = "INSERT INTO Contains (ingredient_id, item_id) VALUES (%s, %s)"
			cursor.execute(statement, [ingr_id, item_id])

		conn.commit()
		cursor.close() 
		conn.close()


		return redirect(url_for('index'))

	message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
	flash(message)
	return redirect(url_for('new_item'))


@app.route('/newsymptom')
def new_symptom():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))
		
	return render_template('newsymptom.html')

@app.route('/addsymptom', methods=['POST','GET'])
def add_symptom():
	input_symptom = request.form['input_symptom']
	input_rating = request.form['input_rating']

	if input_symptom and input_rating:

		conn = mysql.connect()
		cursor = conn.cursor()

		# Insert symptom and then get its id
		statement = "INSERT INTO Symptom (description) VALUES (%s)"
		cursor.execute(statement, [input_symptom])
		query = "SELECT Symptom.symptom_id FROM Symptom WHERE Symptom.description = %s"
		cursor.execute(query, [input_symptom])
		data = cursor.fetchone()
		symptom_id = int(data[0])

		# Insert time and then get its id
		now_date = time.strftime('%Y-%m-%d')
		now_time = time.strftime('%H:%M:%S')
		statement = "INSERT INTO Time (date, time) VALUES (%s, %s)"
		cursor.execute(statement, [now_date, now_time])
		query = "SELECT Time.time_id FROM Time WHERE Time.date = %s AND Time.time = %s"
		cursor.execute(query, [now_date, now_time])
		data = cursor.fetchone()
		time_id = int(data[0])

		# Insert eats relationship using above ids and current user id
		statement = "INSERT INTO Has (time_id, symptom_id, user_id, rating) VALUES (%s, %s, %s, %s)"
		cursor.execute(statement, [time_id, symptom_id, user_id, input_rating])

		conn.commit()
		cursor.close() 
		conn.close()

		return redirect(url_for('index'))

	message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
	flash(message)
	return render_template('newsymptom.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/dologin',methods=['POST','GET'])
def dologin():

	try:
		input_email = request.form['input_email']
		input_password = request.form['input_password']


		# validate the received values
		if input_email and input_password:

			conn = mysql.connect()
			cursor = conn.cursor()

			query = "SELECT User.user_id, User.name, User.password FROM User WHERE User.email = %s"
			cursor.execute(query, [input_email])
			data = cursor.fetchone()

			cursor.close() 
			conn.close()

			if data is None:
				message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')
				flash(message)
				return redirect(url_for('login'))

			
			name = data[1]
			password = data[2]

			if check_password_hash(password, input_password):
				# login_user(unicode(user_id))
				global user_id
				user_id = str(data[0])
				session[user_id] = True
				message = Markup('<div class="flash alert alert-success">Welcome '+name+'!</div>')
				flash(message)
				return redirect(url_for('index'))
			else:
				message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')

		else:
			message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
		
		flash(message)
		return redirect(url_for('login'))
	except Exception as e:
		print e
		message = Markup('<div class="flash alert alert-danger">There was an error signing in.</div>')
		flash(message)
		return redirect(url_for('login'))
		






@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dosignup',methods=['POST','GET'])
def dosignup():
	try:
		input_name = request.form['input_name']
		input_email = request.form['input_email']
		input_password = request.form['input_password']

		conn = mysql.connect()
		cursor = conn.cursor()

		# validate the received values
		if input_name and input_email and input_password:
	
			hashed_password = generate_password_hash(input_password)
			cursor.callproc('sp_createUser',(input_name,input_email,hashed_password))
			data = cursor.fetchall()

			if len(data) is 0:
			    conn.commit()

			    query = "SELECT User.user_id FROM User WHERE User.email = %s"
			    cursor.execute(query, [input_email])
			    result = cursor.fetchone()

			    global user_id
			    user_id = str(result[0])
			    session[user_id] = True
			    message = Markup('<div class="flash alert alert-success">You have been signed up!</div>')
			    flash(message)
			    return redirect(url_for('index'))
			else:
				message = Markup('<div class="flash alert alert-danger">A user with that email already exists.</div>')
		else:
			message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
		
		cursor.close() 
		conn.close()

		flash(message)
		return redirect(url_for('signup'))
	except Exception as e:
		print e
		message = Markup('<div class="flash alert alert-danger">There was an error signing you up.</div>')
		flash(message)
		return redirect(url_for('signup'))
		


@app.route('/logout')
def logout():
	if session.get(user_id):
		session.pop(user_id)
		# logout_user()
		message = Markup('<div class="flash alert alert-info">You have been signed out!</div>')
		flash(message)
	return redirect(url_for('login'))

