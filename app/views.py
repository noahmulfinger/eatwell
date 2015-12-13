from flask import Flask, g, render_template, session, request, redirect, url_for, flash, Markup, jsonify, json
from werkzeug import generate_password_hash, check_password_hash
from app import app, mysql, models #, login_manager

import time

import functions

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
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	user_meals = functions.get_food_items(user_id)
	user_symptoms = functions.get_symptoms(user_id)

	return render_template('index.html', user_meals=user_meals, user_symptoms=user_symptoms)




@app.route('/fooditem/<item_id>')
def get_item(item_id):
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	item = functions.get_food_item(item_id)

	if not item:
		flash(functions.get_flash_message("no_food_item"))
		return redirect(url_for('index'))

	ingredients = functions.get_item_ingredients(item_id)
	badges = functions.get_item_badges(item_id)

	return render_template('fooditem.html', item=item, ingredients=ingredients, badges=badges)


@app.route('/deleteitem', methods=['POST','GET'])
def delete_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_id = request.form['item_id']
	input_time = request.form['item_time']


	functions.delete_food_item(user_id, input_id, input_time)

	flash(functions.get_flash_message("del_item"))
	return redirect(url_for('index'))


@app.route('/deletesymptom', methods=['POST','GET'])
def delete_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_id = request.form['symptom_id']
	input_time = request.form['symptom_time']


	functions.delete_symptom(user_id, input_id, input_time)

	flash(functions.get_flash_message("del_symptom"))
	return redirect(url_for('index'))


@app.route('/newitem')
def new_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	return render_template('newitem.html')

@app.route('/additem', methods=['POST','GET'])
def add_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_name = request.form['input_food_item']
	input_ingr = request.form['input_ingr']
	# input_time = request.form['input_time']

	if input_name and input_ingr:
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		functions.add_food_item(user_id, input_name, input_ingr, now)
		return redirect(url_for('index'))

	flash(functions.get_flash_message("empty_fields"))
	return redirect(url_for('new_item'))


@app.route('/newsymptom')
def new_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	symptoms = functions.get_all_symptoms()
		
	return render_template('newsymptom.html', symptoms=symptoms)

@app.route('/addsymptom', methods=['POST','GET'])
def add_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_symptom = request.form['input_symptom']
	input_rating = request.form['input_rating']
	input_date = request.form['input_date']
	input_time = request.form['input_time']


	if (input_symptom and input_rating and input_date and input_time and 
		input_symptom != 'Select Symptom' and input_rating != 'Select Rating'):
		datetime = input_date + ' ' + input_time
		functions.add_symptom(user_id, input_symptom, input_rating, datetime)
		return redirect(url_for('index'))

	flash(functions.get_flash_message("empty_fields"))
	return redirect(url_for('new_symptom'))


@app.route('/login')
def login():
	return render_template('login.html', logged_out=True)


@app.route('/dologin',methods=['POST','GET'])
def dologin():

	try:
		input_email = request.form['input_email']
		input_password = request.form['input_password']

		if input_email and input_password:
			user = functions.get_user_info(input_email)

			if user is None:
				flash(functions.get_flash_message("bad_login"))
				return redirect(url_for('login'))

			
			password = user['password']

			if check_password_hash(password, input_password):
				# login_user(unicode(user_id))
				global user_id
				user_id = str(user['user_id'])
				global user_name
				user_name = str(user['name'])
				session[user_id] = True
				session[user_name] = True

				flash(functions.get_flash_message("new_login"))
				return redirect(url_for('index'))
			else:
				flash(functions.get_flash_message("bad_login"))
		else:
			flash(functions.get_flash_message("empty_fields"))
		
		return redirect(url_for('login'))
	except Exception as e:
		print e
		flash(functions.get_flash_message("login_error"))
		return redirect(url_for('login'))
		






@app.route('/signup')
def signup():
    return render_template('signup.html', logged_out=True)


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

			flash(functions.get_flash_message("signup"))
			return redirect(url_for('index'))
		else:
			flash(functions.get_flash_message("email_exists"))	
	else:
		flash(functions.get_flash_message("empty_fields"))

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
		flash(functions.get_flash_message("logout"))
	return redirect(url_for('login'))


NAMES=["abc","abcd","abcde","abcdef"]

@app.route('/autocomplete', methods=['POST','GET'])
def autocomplete():
	results = []

	# search = request.args.get('term')
	search = request.form['term']

	search = '%' + str(search) + '%'
	print search
	query = """SELECT Food_Item.name FROM Food_Item WHERE Food_Item.name LIKE %s"""
	result = functions.get_result(query, [search])

	print result
	
	# conn = mysql.connect()
	# cursor = conn.cursor()
	# query = """SELECT Food_Item.name FROM Food_Item WHERE Food_Item.name LIKE %s"""
	# cursor.execute(query, [search])
	# data = cursor.fetchall()
	# print data
	# cursor.close() 
	# conn.close()

	# results.append()
	return json.dumps(result)


# class SearchForm(Form):
# 	function_name = TextField('function_name', validators = [Required()])


