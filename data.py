from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    profile_pic = db.Column(db.LargeBinary)
    twitter = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    instagram = db.Column(db.String(100))

with app.app_context():
    db.create_all()


# Query all users from the database
users = User.query.all()

# Print user details
for user in users:
    print(f"Name: {user.name}\nEmail: {user.email}\nTwitter: {user.twitter}\nLinkedIn: {user.linkedin}\nInstagram: {user.instagram}\n")
