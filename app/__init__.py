from flask import Flask
# from flask.ext.login import LoginManager
from flask.ext.mysql import MySQL
import os

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.urandom(32)

mysql = MySQL()
mysql.init_app(app)

# login_manager = LoginManager()
# login_manager.init_app(app)


from app import views, models
