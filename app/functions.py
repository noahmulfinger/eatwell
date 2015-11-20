from app import mysql

def get_food_items(user_id):
	return get_result("SELECT Food_Item.*, Eats.time \
						FROM Food_Item, Eats \
						WHERE Food_Item.item_id = Eats.item_id \
						AND Eats.user_id = %s", [user_id])

def get_symptoms(user_id):
	return get_result("SELECT Symptom.*, Has.rating, Has.time \
						FROM Symptom, Has \
						WHERE Symptom.symptom_id = Has.symptom_id \
						AND Has.user_id = %s", [user_id])

def get_food_item(item_id):
	return get_result("SELECT Food_Item.* \
						FROM Food_Item \
						WHERE Food_Item.item_id = %s", [item_id])

def get_item_ingredients(item_id):
	return get_result("SELECT Ingredient.* \
						FROM Ingredient, Contains \
						WHERE Contains.item_id = %s \
						AND Ingredient.ingredient_id = Contains.ingredient_id",
						[item_id])

def get_item_badges(item_id):
	return get_result("SELECT Badge.* \
						FROM Badge, Tagged_With \
						WHERE Tagged_With.item_id = %s \
						AND Badge.badge_id = Tagged_With.badge_id",
						[item_id])


def get_user_info(email):
	data = get_result("SELECT User.user_id, User.name, User.password \
						FROM User \
						WHERE User.email = %s",
						[email])
	if len(data) is 0:
		return None
	else:
		return data[0]

def add_food_item(user_id, item_name, ingr_list, time):
	conn = mysql.connect()
	cursor = conn.cursor()

	# Insert into Food_Item, if necessary
	query = "SELECT Food_Item.item_id FROM Food_Item WHERE Food_Item.name = %s"
	statement = "INSERT INTO Food_Item VALUES (0, %s)"
	cursor.execute(query, [item_name])
	data = cursor.fetchone()
	if data is None:
		cursor.execute(statement, [item_name])
		cursor.execute(query, [item_name])
		data = cursor.fetchone()
	item_id = int(data[0])


	# Insert into Eats, if necessary
	query = "SELECT Eats.item_id FROM Eats WHERE Eats.user_id = %s AND Eats.item_id = %s and Eats.time = %s"
	statement = "INSERT INTO Eats VALUES (%s, %s, %s)"
	cursor.execute(query, [user_id, item_id, time])
	data = cursor.fetchone()
	if data is None:
		cursor.execute(statement, [user_id, item_id, time])
		
	# Insert into Ingredients, if necessary
	
	ingr_list = map(str.strip, str(ingr_list).split(','))
	for ingr in ingr_list:
		query = "SELECT Ingredient.ingredient_id FROM Ingredient WHERE Ingredient.name = %s"
		statement = "INSERT INTO Ingredient VALUES (0, %s)"
		cursor.execute(query, [ingr])
		data = cursor.fetchone()
		if data is None:
			cursor.execute(statement, [ingr])
			cursor.execute(query, [ingr])
			data = cursor.fetchone()
		ingr_id = int(data[0])

		# Insert into Contains, if necessary
		query = "SELECT Contains.item_id FROM Contains WHERE Contains.ingredient_id = %s AND Contains.item_id = %s"
		statement = "INSERT INTO Contains VALUES (%s, %s)"
		cursor.execute(query, [ingr_id, item_id])
		data = cursor.fetchone()
		if data is None:
			cursor.execute(statement, [ingr_id, item_id])

	conn.commit()
	cursor.close()
	conn.close()

def delete_food_item(item_id):
	conn = mysql.connect()
	cursor = conn.cursor()

	statement = "DELETE FROM Eats WHERE Eats.item_id = %s"
	cursor.execute(statement, [item_id])

	



def add_symptom(user_id, symptom_name, rating, time):

	conn = mysql.connect()
	cursor = conn.cursor()

	# Insert into Food_Item, if necessary
	query = "SELECT Symptom.symptom_id FROM Symptom WHERE Symptom.description = %s"
	statement = "INSERT INTO Symptom VALUES (0, %s)"
	cursor.execute(query, [symptom_name])
	data = cursor.fetchone()
	if data is None:
		cursor.execute(statement, [symptom_name])
		cursor.execute(query, [symptom_name])
		data = cursor.fetchone()
	symptom_id = int(data[0])

	# Insert into Eats, if necessary
	query = "SELECT Has.symptom_id FROM Has WHERE Has.symptom_id = %s AND Has.user_id = %s AND Has.rating = %s AND Has.time = %s"
	statement = "INSERT INTO Has VALUES (%s, %s, %s, %s)"
	cursor.execute(query, [symptom_id, user_id, rating, time])
	data = cursor.fetchone()
	if data is None:
		cursor.execute(statement, [symptom_id, user_id, rating, time])

	conn.commit()
	cursor.close()
	conn.close()


def sign_up_user(name, email, password):
	conn = mysql.connect()
	cursor = conn.cursor()

	# query = "SELECT User.user_id FROM User WHERE User.email = %s"
	statement = "INSERT INTO User VALUES (0, %s, %s, %s)"
	cursor.execute(statement, [name, email, password])
	# cursor.execute(query, [email])
	# data = cursor.fetchone()

	conn.commit()
	cursor.close() 
	conn.close()

	# return str(data[0])

# Returns array of dictionary objects based on query
def get_result(query, values):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(query, values)
	data = []
	row = row_to_dict(cursor)
	
	while row is not None:
		data.append(row)
		row = row_to_dict(cursor)

	cursor.close() 
	conn.close()
	return data

# Converts individual tuple into dictionary
def row_to_dict(cursor):
	data = cursor.fetchone()
	desc = cursor.description
	if data is None:
		return None
	dict = {}
	for (name, value) in zip(desc, data):
		dict[name[0]] = value
	return dict


