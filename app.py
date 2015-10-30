from flask import Flask, render_template, request, json, session, redirect, url_for, flash, Markup
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os
app = Flask(__name__)

# CHANGE THIS TO RANDOM VALUE!!!! IT WAS COPIED FROM TUTORIAL
app.secret_key = os.urandom(32)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'eatwell'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
@app.route('/home')
def showHome():

	if not session.get('signed_in'):
		message = Markup('<div class="flash alert alert-danger">You are not signed in.</div>')
		flash(message)
		return redirect(url_for('signIn'))

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

##
## TODO: Fix rendering of html going to console
##       happens becuase js logs response to console
## 		 Think about removing javascript and following tutorial
##


@app.route('/dosignin',methods=['POST','GET'])
def doSignIn():

	try:
		inputEmail = request.form['inputEmail']
		inputPassword = request.form['inputPassword']


		# validate the received values
		if inputEmail and inputPassword:

			conn = mysql.connect()
			cursor = conn.cursor()

			query = "SELECT User.name, User.password FROM User WHERE User.email = %s"
			cursor.execute(query, [inputEmail])
			data = cursor.fetchone()

			if data is None:
				message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')
				flash(message)
				return redirect(url_for('signIn'))

			name = data[0]
			password = data[1]

			if check_password_hash(password, inputPassword):
				session['signed_in'] = True
				message = Markup('<div class="flash alert alert-success">Sign in successful!</div>')
				flash(message)
				return redirect(url_for('showHome'))
			else:
				message = Markup('<div class="flash alert alert-danger">Incorrect email and/or password.</div>')
				flash(message)
				return redirect(url_for('signIn'))

		else:
			message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
			flash(message)
			return redirect(url_for('signIn'))
	except Exception as e:
		message = Markup('<div class="flash alert alert-danger">There was an error signing in.</div>')
		flash(message)
		return redirect(url_for('signIn'))
	finally:
		cursor.close() 
		conn.close()






@app.route('/signup')
def signUp():
    return render_template('signup.html')


@app.route('/dosignup',methods=['POST','GET'])
def doSignUp():
	try:
		inputName = request.form['inputName']
		inputEmail = request.form['inputEmail']
		inputPassword = request.form['inputPassword']

		# validate the received values
		if _name and _email and _password:

			# All Good, let's call MySQL

			conn = mysql.connect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser',(inputName,inputEmail,inputPassword))
			data = cursor.fetchall()

			if len(data) is 0:
			    conn.commit()
			    session['signed_in'] = True
			    message = Markup('<div class="flash alert alert-success">You have been signed up!</div>')
			    flash(message)
			    return redirect(url_for('showHome'))
			else:
				message = Markup('<div class="flash alert alert-danger">A user with that email already exists.</div>')
				flash(message)
				return redirect(url_for('signUp'))
		else:
			message = Markup('<div class="flash alert alert-danger">Please fill out all fields.</div>')
			flash(message)
			return redirect(url_for('signUp'))
	except Exception as e:
		message = Markup('<div class="flash alert alert-danger">There was an error signing in.</div>')
		flash(message)
		return redirect(url_for('signUp'))
	finally:
		cursor.close() 
		conn.close()


@app.route('/signout')
def signOut():
	session.pop('signed_in', None)
	message = Markup('<div class="flash alert alert-info">You have been signed out!</div>')
	flash(message)
	return redirect(url_for('signIn'))



if __name__ == "__main__":
    app.run(debug = True)







