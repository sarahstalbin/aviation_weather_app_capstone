#from flask import Flask, render_template, request, session
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from forms import LoginForm
from flask_login import login_user, logout_user, login_required
from models import db, login_manager, UserModel
from api import get_wind_temp_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

def add_user(email, password):
    user = UserModel(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

@app.route('/home')
def home():
    return render_template('home.html', windTemp = get_wind_temp_data())

@app.route('/login')
def login():
    return render_template('login.html', windTemp = get_wind_temp_data())

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True', port=5000)