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

global user_name
user_name = None

@app.route('/')
@app.route('/index')
# @login_required
def index():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	user_meals = functions.get_food_items(user_id)
	user_symptoms = functions.get_symptoms(user_id)

	return render_template('index.html', user_meals=user_meals, user_symptoms=user_symptoms)




@app.route('/fooditem/<item_id>')
def get_item(item_id):
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	item = functions.get_food_item(item_id)

	if not item:
		message = Markup('<div class="flash alert alert-danger">Food item does not exist.</div>')
		flash(message)
		return redirect(url_for('index'))

	ingredients = functions.get_item_ingredients(item_id)
	badges = functions.get_item_badges(item_id)

	return render_template('fooditem.html', item=item, ingredients=ingredients, badges=badges)


@app.route('/delete/<item_id>')
def delete_item(item_id):
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	functions.delete_food_item(item_id)

	return render_template('index.html')

@app.route('/newitem')
def new_item():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	return render_template('newitem.html')

@app.route('/additem', methods=['POST','GET'])
def add_item():
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	input_name = request.form['input_food_item']
	input_ingr = request.form['input_ingr']
	# input_time = request.form['input_time']

	if input_name and input_ingr:
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		functions.add_food_item(user_id, input_name, input_ingr, now)
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
	if not session.get(user_id):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('login'))

	input_symptom = request.form['input_symptom']
	input_rating = request.form['input_rating']
	# input_time = request.form['input_time']

	if input_symptom and input_rating:
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		functions.add_symptom(user_id, input_symptom, input_rating, now)
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

		if input_email and input_password:
			user = functions.get_user_info(input_email)

			if user is None:
				message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')
				flash(message)
				return redirect(url_for('login'))

			
			password = user['password']

			if check_password_hash(password, input_password):
				# login_user(unicode(user_id))
				global user_id
				user_id = str(user['user_id'])
				global user_name
				user_name = user['name']
				session[user_id] = True

				message = Markup('<div class="flash alert alert-success">Welcome '+user_name+'!</div>')
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
	# try:
	input_name = request.form['input_name']
	input_email = request.form['input_email']
	input_password = request.form['input_password']

	if input_name and input_email and input_password:
		hashed_password = generate_password_hash(input_password)
		user = functions.get_user_info(input_email)

		if user is None:

			functions.sign_up_user(input_name, input_email, hashed_password)
			user = functions.get_user_info(input_email)

			global user_id
			user_id = str(user['user_id'])
			global user_name
			user_name = user['name']
			session[user_id] = True

			message = Markup('<div class="flash alert alert-success">You have been signed up!</div>')
			flash(message)
			return redirect(url_for('index'))
		else:
			message = Markup('<div class="flash alert alert-danger">A user with that email already exists.</div>')		
	else:
		message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')

	flash(message)
	return redirect(url_for('signup'))
	# except Exception as e:
	# 	print e
	# 	message = Markup('<div class="flash alert alert-danger">There was an error signing you up.</div>')
	# 	flash(message)
	# 	return redirect(url_for('signup'))
		


@app.route('/logout')
def logout():
	if session.get(user_id):
		session.pop(user_id)
		session.pop(user_name)
		# logout_user()
		message = Markup('<div class="flash alert alert-info">You have been signed out!</div>')
		flash(message)
	return redirect(url_for('login'))

