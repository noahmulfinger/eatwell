from flask import Flask, g, render_template, session, request, redirect, url_for, flash, Markup
from werkzeug import generate_password_hash, check_password_hash
from app import app, mysql, models #, login_manager

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

	conn = mysql.connect()
	cursor = conn.cursor()
	
	#Entities
	users = get_data("SELECT User.user_id, User.name, User.email FROM User", cursor)
  	food_items = get_data("SELECT Food_Item.item_id, Food_Item.name FROM Food_Item", cursor)
  	times = get_data("SELECT Time.time_id, Time.date, Time.time FROM Time", cursor)
  	symptoms = get_data("SELECT Symptom.symptom_id, Symptom.description FROM Symptom", cursor)
  	badges = get_data("SELECT Badge.badge_id, Badge.name FROM Badge", cursor)
  	ingredients = get_data("SELECT Ingredient.ingredient_id, Ingredient.name FROM Ingredient", cursor)
	
	#Relationships
	eats = get_data("SELECT * FROM Eats", cursor)
	has = get_data("SELECT * FROM Has", cursor)
	tagged = get_data("SELECT * FROM Tagged_With", cursor)
	contains = get_data("SELECT * FROM Contains", cursor)
	caused = get_data("SELECT * FROM Caused_By", cursor)

	user_meals = get_data_with_vals("SELECT Food_Item.* FROM Food_Item, Eats, User WHERE Food_Item.item_id = Eats.item_id AND Eats.user_id = %s", [user_id], cursor)

	cursor.close() 
	conn.close()

	return render_template('index.html', users=users, food_items=food_items, times=times, eats=eats, user_meals=user_meals)

def get_data(query, cursor):
	cursor.execute(query)
	data = []
	row = row_to_dict(cursor)
	while row is not None:
		data.append(row)
		row = row_to_dict(cursor)
	return data

def get_data_with_vals(query, values, cursor):
	cursor.execute(query, values)
	data = []
	row = row_to_dict(cursor)
	while row is not None:
		data.append(row)
		row = row_to_dict(cursor)
	return data


def row_to_dict(cursor):
	data = cursor.fetchone()
	desc = cursor.description
	if data is None:
		return None
	dict = {}
	for (name, value) in zip(desc, data):
		dict[name[0]] = value
	return dict

@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/dologin',methods=['POST','GET'])
def dologin():

	# user = User.get(request.form['input_email'], request.form['input_password'])

	# if user:
	# 	login_user(user)
	# 	message = Markup('<div class="flash alert alert-success">Login successful!</div>')
	# 	flash(message)
	# 	return redirect(url_for('index'))
	# else:
	# 	message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')
	# 	flash(message)
	# 	return redirect(url_for('login'))


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
				# flash(message)
				# return redirect(url_for('login'))

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
	session.pop(user_id)
	# logout_user()
	message = Markup('<div class="flash alert alert-info">You have been signed out!</div>')
	flash(message)
	return redirect(url_for('login'))

