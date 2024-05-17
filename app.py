from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/logout')
def logout():
    return render_template('logout.html') 