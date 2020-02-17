from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='ae90f4edaff92b5def4ddea3e2d65041'
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskapp.users.routes import users
from flaskapp.posts.routes import posts
from flaskapp.main.routes import main

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)