#!/usr/bin/env python3
# Import the necessary modules
import os
from flask import Flask, render_template, request, session, redirect, flash, url_for
from forms import LoginForm, UpdateEmailForm, RegisterForm, DeleteAccountForm, ChangePasswordForm
from forms import LoginForm, RegisterForm
from api_sfo import get_wind_temp_data
from plot_data import plotting
from flask_login import login_user, logout_user, login_required, current_user
from models import db, login_manager, UserModel, load_user
from flask import request

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
@app.before_request
def create_db():
    db.create_all()
    if not UserModel.query.filter_by(email='abc@uw.edu').first():
        add_user('abc@uw.edu', 'password')

@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/map')
def map():
    return render_template('map.html')
  

@app.route('/plot', methods=['GET'])
def plot():
    if request.method == 'GET' and 'data_state' in request.args and request.args.get('data_state') is not None:
        session['data_state'] = request.args.get('data_state')
        print("data_state", session['data_state'])
    if request.method == 'GET' and 'city' in request.args and request.args.get('city') is not None:
        session['city'] = request.args.get('city')
    if request.method == 'GET' and 'weather' in request.args and request.args.get('weather') is not None:
        session['weather'] = request.args.get('weather')
    if 'data_state' in session:
        past_type = session.get('data_state')
    else:
        past_type = 'past'
    
    if 'city' in session:
        city_type = session.get('city')
    else:
        city_type = 'Seattle'

    if 'weather' in session:
        weather_type = session.get('weather')
    else:
        weather_type = 'temp'
    return render_template('plot.html', graph_html=plotting(location=city_type, type=weather_type, current_state=past_type))  

# Define a route for the root URL ("/") that returns "Hello World"
@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    if request.method == 'GET' and 'sites' in request.args and request.args.get('sites') is not None:
        session['sites'] = request.args.get('sites')
    if 'sites' in session:
        return render_template('dashboard.html', sites=get_wind_temp_data(di=session['sites']))
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    user_exists = False
    if form.validate_on_submit():
        if UserModel.query.filter_by(email=form.email.data).first():
            flash('Email address already registered', 'danger')
            return redirect(url_for('register'))
        user = UserModel(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful, please log in.', 'success')
        user_exists = True
        session.clear()
        return redirect(url_for('registration_confirmed'))
    return render_template('register.html', form=form, user_exists=user_exists)

@app.route('/registration_confirmed')
def registration_confirmed():
    return render_template('registration_confirmed.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/account')
@login_required
def account():
    form = DeleteAccountForm()
    return render_template('account.html', email=current_user.email, form=form)

@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    form = DeleteAccountForm()
    if form.validate_on_submit():
        user  = current_user
        db.session.delete(user)
        db.session.commit()
        flash('Your account has been deleted', 'success')
        logout()
        return redirect(url_for('home'))
    return render_template('delete_account.html', form=form)

@app.route('/update_email', methods=['GET', 'POST'])
@login_required
def update_email():
    form = UpdateEmailForm()
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        flash('Your email address has been updated', 'success')
        return redirect(url_for('account'))
    return render_template('update_email.html', email=current_user.email, form=form)

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('Old password is incorrect.', 'danger')
        else:
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Your password has been updated.', 'success')
            return redirect(url_for('account'))
    return render_template('change_password.html', form=form)


# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
