from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class users(db.Model):
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




if __name__ == "__main__" :
    app.run(debug=True)