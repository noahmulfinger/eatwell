from flask import Flask, g, render_template, session, request, redirect, url_for, flash, Markup, jsonify, json
from werkzeug import generate_password_hash, check_password_hash
from app import app, mysql, models
import time, re
import functions

global user_id
user_id = None

global user_name
user_name = None

global symptom_search
symptom_search = None

@app.route('/')
@app.route('/index')
# @login_required
def index():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	user_meals = functions.get_food_items_index(user_id)
	user_symptoms = functions.get_symptoms(user_id)

	return render_template('index.html', user_meals=user_meals, user_symptoms=user_symptoms, isIndex = True)

@app.route('/searchbydate', methods=['POST'])
def searchbydate():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	date = request.form['date']
	date_items = functions.search_food_by_date(user_id, date)
	date_symptoms = functions.search_symptoms_by_date(user_id,date)

	return render_template('date.html', user_meals = date_items, user_symptoms=date_symptoms)



@app.route('/searchbyfood', methods=['POST'])
def searchbyfood():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	item_search = request.form['search']
	found_items = functions.search_food_by_name(item_search, user_id)

	return render_template('index.html', user_meals = found_items, user_symptoms = [], isIndex = False)

@app.route('/searchbysymptom', methods=['POST'])
def searchbysymptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	global symptom_search
	symptom_search = request.form['search']

	order = "description"
	sorted_search_symptoms = functions.get_found_symptoms_ordered(user_id, order, symptom_search)

	return render_template('found_symptoms.html', user_symptoms=sorted_search_symptoms)



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


@app.route('/deleteitem', methods=['POST'])
def delete_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_id = request.form['item_id']
	input_time = request.form['item_time']


	functions.delete_food_item(user_id, input_id, input_time)

	flash(functions.get_flash_message("del_item"))
	return redirect(url_for('index'))


@app.route('/deletesymptom', methods=['POST'])
def delete_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_id = request.form['symptom_id']
	input_time = request.form['symptom_time']


	functions.delete_symptom(user_id, input_id, input_time)

	flash(functions.get_flash_message("del_symptom"))
	return redirect(url_for('index'))


@app.route('/newitem', methods=['POST'])
def new_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))


	back_url = request.form['back_url']

	query = "SELECT Food_Item.name FROM Food_Item"
	results = functions.get_result(query, [])

	new_results = []

	for r in results:
		new_results.append(str(r['name']))

	return render_template('newitem.html', food_items=json.dumps(new_results), back_url=back_url)

@app.route('/additem', methods=['POST'])
def add_item():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_name = request.form['input_food_item']
	input_ingr = request.form.getlist('input_ingr[]')

	print input_ingr

	fItems = []
	for i in input_ingr:
		fItems.append(str(i))

	datetime = request.form['datetime']
	back_url = request.form['back_url']

	if input_name and input_ingr and datetime:

		datetime = datetime + ':00'

		functions.add_food_item(user_id, input_name, fItems, datetime)
		flash(functions.get_flash_message("add_item"))
		return redirect(url_for(back_url))

	flash(functions.get_flash_message("empty_fields"))
	return redirect(url_for('new_item'))


@app.route('/fooditems', methods=['GET'])
def show_food_items():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	order = 'time'

	if 'sortBy' in request.args:
		order = request.args['sortBy']

	user_food_items = functions.get_items_ordered(user_id, order)

	return render_template('fooditems.html', user_food_items=user_food_items)


@app.route('/symptoms', methods=['GET'])
def show_symptoms():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	order = 'time'

	if 'sortBy' in request.args:
		order = request.args['sortBy']

	user_symptoms = functions.get_symptoms_ordered(user_id, order)

	return render_template('symptoms.html', user_symptoms=user_symptoms)

@app.route('/order_found_symptoms', methods=['GET'])
def order_found_symptoms():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	order = 'time'

	if 'sortBy' in request.args:
		order = request.args['sortBy']

	sorted_search_symptoms = functions.get_found_symptoms_ordered(user_id, order, symptom_search)

	return render_template('found_symptoms.html', user_symptoms=sorted_search_symptoms)


@app.route('/newsymptom', methods=['POST'])
def new_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	back_url = request.form['back_url']

	symptoms = functions.get_all_symptoms()
		
	return render_template('newsymptom.html', symptoms=symptoms, back_url=back_url)

@app.route('/addsymptom', methods=['POST'])
def add_symptom():
	if not session.get(user_id):
		flash(functions.get_flash_message("not_logged_in"))
		return redirect(url_for('login'))

	input_symptom = request.form['input_symptom']
	input_rating = request.form['input_rating']
	datetime = request.form['datetime']
	back_url = request.form['back_url']

	if (input_symptom and input_rating and datetime and 
		input_symptom != 'Select Symptom' and input_rating != 'Select Rating'):
		
		datetime = datetime + ':00'

		functions.add_symptom(user_id, input_symptom, input_rating, datetime)
		flash(functions.get_flash_message("add_symptom"))
		return redirect(url_for(back_url))

	flash(functions.get_flash_message("empty_fields"))
	return redirect(url_for('new_symptom'))


@app.route('/login')
def login():
	return render_template('login.html', logged_out=True)


@app.route('/dologin',methods=['POST'])
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


@app.route('/dosignup',methods=['POST'])
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


@app.route('/test')
def test():
	query = "SELECT Food_Item.name FROM Food_Item"
	results = functions.get_result(query, [])

	newResults = []

	for r in results:
		newResults.append(str(r['name']))

	return render_template('test.html', food_items=json.dumps(newResults))

@app.route('/autocomplete_ingr/<food_item>', methods=['GET'])
def autocomplete_ingredients(food_item):

	results = []

	# search = request.args.get('term')
	

	search = '%' + str(food_item) + '%'


	# print search
	query = """SELECT Food_Item.item_id FROM Food_Item WHERE Food_Item.name LIKE %s"""
	result = functions.get_result(query, [search])



	if result is None:
		return []

	all_ingr = []


	for i in range(len(result)):
		ingr_list = functions.get_item_ingredients(result[i]["item_id"])
		for ingredient in ingr_list:
			all_ingr.append(ingredient["name"])

	all_ingr_names = list(set(all_ingr))

	return json.dumps(all_ingr_names)

# class SearchForm(Form):
# 	function_name = TextField('function_name', validators = [Required()])


