from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='ae90f4edaff92b5def4ddea3e2d65041'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from flaskapp.users.routes import users
from flaskapp.master.routes import master
from flaskapp.main.routes import main
from flaskapp.notifications.routes import notifications

app.register_blueprint(main)
app.register_blueprint(master)
app.register_blueprint(users)
app.register_blueprint(notifications)