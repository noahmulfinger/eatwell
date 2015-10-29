from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'eatwell'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
@app.route('/index')
def main():

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT User.name, User.email from User")
	
	users = []
	row = rowToDict(cursor)
	while row is not None:
  		users.append(row)
  		row = rowToDict(cursor)

	cursor.close() 
	conn.close()

	return render_template('index.html', users=users)

def rowToDict(cursor):
	data = cursor.fetchone()
	desc = cursor.description
	if data == None:
		return None
	dict = {}
	for (name, value) in zip(desc, data):
		dict[name[0]] = value
	return dict


@app.route('/signin')
def signIn():
	return render_template('signin.html')


@app.route('/dosignin',methods=['POST','GET'])
def doSignIn():


	inputEmail = request.form['inputEmail']
	inputPassword = request.form['inputPassword']


	# validate the received values
	if _email and _password:

		conn = mysql.connect()
		cursor = conn.cursor()

		query = "SELECT User.name, User.password FROM User WHERE User.email = %s"
		cursor.execute(query, [inputEmail])
		data = cursor.fetchone()
		cursor.close() 
		conn.close()

		if data is None:
			return json.dumps({'message':'No user found!'})

		name = data[0]
		password = data[1]

		if check_password_hash(password, inputPassword):
			return json.dumps({'message':'Sign in successful !'})
		else:
			return json.dumps({'message':'Incorrect password'})

	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})




@app.route('/signup')
def signUp():
    return render_template('signup.html')


@app.route('/dosignup',methods=['POST','GET'])
def doSignUp():
	try:
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']

		# validate the received values
		if _name and _email and _password:

			# All Good, let's call MySQL

			conn = mysql.connect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
			data = cursor.fetchall()

			if len(data) is 0:
			    conn.commit()
			    return json.dumps({'message':'User created successfully !'})
			else:
			    return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close() 
		conn.close()





if __name__ == "__main__":
    app.run(debug = True)







