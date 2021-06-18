from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app= Flask(__name__)

# secret key so that no one modify the cookies: # find it from python get_hex() :-
app.config['SECRET_KEY']='4b7334042a2a36585ed3bacfddb06e43'

# to setup database  url:
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'

db= SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category='info'

from flaskblog import routes
