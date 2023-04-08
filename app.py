from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def home():
    
    return render_template('index.html')

@app.route('/login')
def login():
    
    return render_template('login.html')




if __name__ == "__main__" :
    app.run(debug=True)