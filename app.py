#!/usr/bin/env python3
# Import the necessary modules
import os
from flask import Flask, render_template, request, session, redirect, flash, url_for
from forms import LoginForm
from api_sfo import get_wind_temp_data
from flask_login import login_user, logout_user, login_required 
from models import db, login_manager, UserModel

# Create a new Flask application instance
app = Flask(__name__)
app.secret_key='super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

#add user routine
def add_user(email, password):
    user = UserModel(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user
# create database with a test user
@app.before_first_request
def create_db():
    db.create_all()
    #if (not os.path.exisits('login.db')):
    add_user('abc@uw.edu', 'password')

@app.route('/home')
def home():
    return render_template('base.html')

# Define a route for the root URL ("/") that returns "Hello World"
@app.route('/user_home', methods=['GET'])
def user():
    if request.method == 'GET' and 'sites' in request.args and request.args.get('sites') is not None:
        session['sites'] = request.args.get('sites')
    if 'sites' in session:
        return render_template('logged_in_home.html', sites=get_wind_temp_data(di=session['sites']))
    return render_template('logged_in_home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    return render_template('login.html',form=form)

# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)
