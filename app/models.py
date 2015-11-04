# from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
# from werkzeug import generate_password_hash, check_password_hash

# from app import app, mysql, login_manager

# class UserNotFoundError(Exception):
#     pass

# class IncorrectPasswordError(Exception):
#     pass

# class User(UserMixin):

# 	def __init__(self, email, password):

# 		conn = mysql.connect()
# 		cursor = conn.cursor()

# 		query = "SELECT User.user_id, User.name, User.password FROM User WHERE User.email = %s"
# 		cursor.execute(query, [email])
# 		data = cursor.fetchone()

# 		cursor.close() 
# 		conn.close()

# 		if data is None:
# 			raise UserNotFoundError()

# 		if not check_password_hash(data[2], password):
# 			raise IncorrectPasswordError()

# 		self.id = data[0]
# 		self.name = data[1]
# 		self.email = email

# 	@classmethod
# 	def get(self_class, email, password):
# 	    try:
# 	        return self_class(email, password)
# 	    except UserNotFoundError:
# 	        return None
# 	    except IncorrectPasswordError:
# 	    	return None

# @login_manager.user_loader
# def load_user(email, password):
#     return User.get(email, password)