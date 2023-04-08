from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile_pic = db.Column(db.LargeBinary, nullable=False)
    twitter = db.Column(db.String(120), nullable=True)
    linkedin = db.Column(db.String(120), nullable=True)
    instagram = db.Column(db.String(120), nullable=True)
    
    def __repr__(self):
        return '<User %r>' % self.name


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        profile_pic = request.files['profile_pic']
        twitter = request.form['twitter']
        linkedin = request.form['linkedin']
        instagram = request.form['instagram']

        # Save the uploaded profile pic to the uploads folder
        filename = secure_filename(profile_pic.filename)
        profile_pic_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        profile_pic.save(profile_pic_path)

        # Create a new User object and add it to the database
        user = User(name=name, email=email, password=password, profile_pic=open(profile_pic_path, 'rb').read(), twitter=twitter, linkedin=linkedin, instagram=instagram)
        db.session.add(user)
        db.session.commit()
        
        return 'Thanks for signing up!'






if __name__ == "__main__" :
    app.run(debug=True)