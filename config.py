from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Blog, Comment, PhotoProfile
from flask_migrate import Migrate, MigrateCommand
