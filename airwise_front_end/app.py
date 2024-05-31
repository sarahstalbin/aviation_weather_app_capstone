from flask import Flask, render_template, request, session, redirect, flash, url_for, jsonify
from flask_login import login_user, logout_user, login_required
from models import db, login_manager, UserModel, load_user
from api_sfo import get_sfo, get_hawaii, get_all, get_alaska, get_other_pac, get_south_central, get_north_central, get_rocky_mountain, get_south_east, get_north_east
from api_metars import get_metar
from forms import LoginForm, RegisterForm
app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)
# Add user routine
def add_user(email, password):
    user = UserModel(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

# Create database with a test user
@app.before_request
def create_db():
    db.create_all()
    if not UserModel.query.filter_by(email='abc@uw.edu').first():
        add_user('abc@uw.edu', 'password')
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    region = request.args.get('region', 'sfo')
    fcst = request.args.get('fcst', '06')
    level = request.args.get('level', 'low')
    get_metar_flag = request.args.get('get_metar', None)
#    print(region,fcst,level)
    app.logger.info(f'Region: {region}, Forecast: {fcst}, Level: {level}')

    if region == 'sfo':
        wind_temp_data = get_sfo(region=region, level=level, fcst=fcst)
    elif region == 'other_pac':
        wind_temp_data = get_other_pac(region=region, level=level, fcst=fcst)
    elif region == 'hawaii':
        wind_temp_data = get_hawaii(region=region, level=level, fcst=fcst)
    elif region == 'all':
        wind_temp_data = get_all(region=region, level=level, fcst=fcst)
    elif region == 'alaska':
        wind_temp_data = get_alaska(region=region, level=level, fcst=fcst)
    elif region == 'bos':
        wind_temp_data = get_north_east(region=region, level=level, fcst=fcst)
    elif region == 'mia':
        wind_temp_data = get_south_east(region=region, level=level, fcst=fcst)
    elif region == 'chi':
        wind_temp_data = get_north_central(region=region, level=level, fcst=fcst)
    elif region == 'dfw':
        wind_temp_data = get_south_central(region=region, level=level, fcst=fcst)
    elif region == 'slc':
        wind_temp_data = get_rocky_mountain(region=region, level=level, fcst=fcst)

    else:
        pass

    metar_data = get_metar(ids="@WA", format="json", taf="1", hours="10", bbox="40,-90,45,-85", date="20240531_144001Z") if get_metar_flag else None
    
    return render_template('dashboard.html', wind_temp_data=wind_temp_data, metar_data = metar_data,  region=region, fcst=fcst, level=level)

@app.route('/get_wind_temp', methods=['GET'])
@login_required
def get_wind_temp():
    region = request.args.get('region', 'sfo')
    fcst = request.args.get('fcst', '06')
    level = request.args.get('level', 'low')

    app.logger.info(f'Region: {region}, Forecast: {fcst}, Level: {level}')
    
    if region == 'sfo':
        data = get_sfo(region=region, level=level, fcst=fcst)
    elif region == 'other_pac':
        data = get_other_pac(region=region, level=level, fcst=fcst)
    elif region == 'hawaii':
        data = get_hawaii(region=region, level=level, fcst=fcst)
    elif region == 'all':
        data = get_all(region=region, level=level, fcst=fcst)
    elif region == 'alaska':
        data = get_alaska(region=region, level=level, fcst=fcst)
    elif region == 'bos':
        data = get_north_east(region=region, level=level, fcst=fcst)
    elif region == 'mia':
        data = get_south_east(region=region, level=level, fcst=fcst)
    elif region == 'chi':
        data = get_north_central(region=region, level=level, fcst=fcst)
    elif region == 'dfw':
        data = get_south_central(region=region, level=level, fcst=fcst)
    elif region == 'slc':
        data = get_rocky_mountain(region=region, level=level, fcst=fcst)


    else:
        pass
    
    return jsonify(data)

@app.route('/get_metars', methods=['GET'])
@login_required  
#@app.route('/get_metars', methods=['GET'])
def get_metars():
  """
  API endpoint to retrieve METAR data.

  Returns:
      JSON: Dictionary containing METAR data or an error message.
  """
  # Get parameters from the request (modify as needed)
  ids = request.args.get('ids', "@WA")  # Default to WA stations
  format = request.args.get('format', 'json')
  taf = request.args.get('taf', '1')
  hours = request.args.get('hours', '10')
  bbox = request.args.get('bbox')  # Optional bounding box
  date = request.args.get('date')  # Optional date

  # Call your get_metar function with retrieved parameters
  metar_data = get_metar(ids=ids, format=format, taf=taf, hours=hours, bbox=bbox, date=date)

  if metar_data:
    return jsonify(metar_data)
  else:
    return jsonify({"error": "Failed to retrieve METAR data"}), 400  # Return error with status code 400 (Bad Request)

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
        return redirect(url_for('login'))
    return render_template('register.html', form=form, user_exists=user_exists)

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
# Run the application if this script is being run directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

