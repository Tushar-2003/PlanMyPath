from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_BINDS'] = {
    'roadmaps': 'sqlite:///roadmaps.db',
    'path': 'sqlite:///path.db'
}
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


class Roadmap(db.Model):
    __bind_key__ = 'roadmaps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    # image = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return '<Roadmap %r>' % self.name

class Path(db.Model):
    __bind_key__ = 'path'
    id =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Path {self.id}: {self.title}>'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', )
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists in the database
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect('/')
        else:
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
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
        
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/create',methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        
        roadmap = Roadmap(name=name, desc=desc)
        
        db.session.add(roadmap)
        db.session.commit()
        
        return redirect(url_for('index'))
        

    return render_template('create.html')







if __name__ == "__main__" :
    app.run(debug=True)