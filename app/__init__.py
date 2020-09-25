from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from config import config_options
from flask_mail import Mail
from flask_simplemde import SimpleMDE


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)

mail = Mail()
simple = SimpleMDE()