from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Quote:
    '''
    Quote class to hold random quote
    '''

    def __init__(self, author, quote, permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink