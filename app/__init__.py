from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from config import config_options
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_mail import Mail, Message
from flask_simplemde import SimpleMDE
# import sys
# import logging


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)

mail = Mail()
simple = SimpleMDE()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Intializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)
    csrf = CSRFProtect(app)


    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)
    

    return app