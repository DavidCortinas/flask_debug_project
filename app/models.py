from app import app, db, login

# Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
# Import for Date Time Module
from datetime import datetime

#Imports for Login manager and User Mixin
from flask_login import UserMixin, current_user

# Create the current user_manager using the user_login function
# Which is a decorator (used in this case as callback function)
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    post = db.relationship('Post', backref = 'user', lazy = True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password): 
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return f'{self.username} has been created with {self.email}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}.'