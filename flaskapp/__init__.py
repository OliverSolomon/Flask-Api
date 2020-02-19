from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskapp.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class = Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flaskapp.users.routes import users
    from flaskapp.master.routes import master
    from flaskapp.main.routes import main
    from flaskapp.notifications.routes import notifications
    app.register_blueprint(main)
    app.register_blueprint(master)
    app.register_blueprint(users)
    app.register_blueprint(notifications)

    return app
