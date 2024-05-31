from flask import Flask, render_template, request, session, redirect, flash, url_for, jsonify
from flask_login import login_user, logout_user, login_required
from models import db, login_manager, UserModel, load_user
from api_sfo import get_sfo
from api_other_pac import get_wind_temp_data
from api_obs import get_obstacle_data
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
#@app.route('/dashboard', methods=['GET'])
#@login_required
#def dashboard():
 #   region = request.args.get('region', 'sfo')
  #  fcst = request.args.get('fcst', '06')
   # level = request.args.get('level', 'low')
    
   # app.logger.info(f'Region: {region}, Forecast: {fcst}, Level: {level}')

   # wind_temp_data = None
   # if region in ('sfo', 'other_pac', 'all'):  # Check for valid regions
    #    if region == 'sfo':
     #       if fcst == '06':
      #          wind_temp_data = get_sfo_low_06(region=region, level=level, fcst=fcst)
       #     elif fcst == '12':
        #        wind_temp_data = get_sfo_low_12(region=region, level=level, fcst=fcst)
         #   elif fcst == '24':
          #      wind_temp_data = get_sfo_low_24(region=region, level=level, fcst=fcst)
        #elif region == 'other_pac':
         #   wind_temp_data = get_wind_temp_data(region=region, level=level, fcst=fcst)
       # else:  # Handle 'all' region (assuming combining data)
            # Implement logic to combine data from both regions (if applicable)
        #    pass  # Replace with code to combine data from SFO and other_pac

   # else:
        # No data for invalid regions
    #    wind_temp_data = []  # Set to empty list for clarity

   # obstacle_data = get_obstacle_data(bbox="40,-90,45,-85")

    # Populate the context dictionary
   # context = {
    #    'wind_temp_data': wind_temp_data,
     #   'obstacle_data': obstacle_data,
      #  'region': region,
       # 'fcst': fcst,
       # 'level': level
   # }

   # return render_template('dashboard.html', **context)

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    region = request.args.get('region', 'sfo')
    fcst = request.args.get('fcst', '06')
    level = request.args.get('level', 'low')
    print(region,fcst,level)
    app.logger.info(f'Region: {region}, Forecast: {fcst}, Level: {level}')

    if region == 'sfo':
        wind_temp_data = get_sfo(region=region, level=level, fcst=fcst)
    elif region == 'other_pac':
        wind_temp_data = get_wind_temp_data(region=region, level=level, fcst=fcst)
    else:
        pass
        # Assuming you want to combine data from both regions if 'all' is selected
    #    wind_temp_data = get_sfo_data(region='sfo', level=level, fcst=fcst) + get_other_pac_data(region='other_pac', level=level, fcst=fcst)

    obstacle_data = get_obstacle_data(bbox="40,-90,45,-85")
    
    return render_template('dashboard.html', wind_temp_data=wind_temp_data, obstacle_data=obstacle_data, region=region, fcst=fcst, level=level)

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
        data = get_wind_temp_data(region=region, level=level, fcst=fcst)
    else:
        pass
        # Assuming you want to combine data from both regions if 'all' is selected
 #       data = get_sfo_data(region='sfo', level=level, fcst=fcst) + get_other_pac_data(region='other_pac', level=level, fcst=fcstt)
    
    return jsonify(data)

@app.route('/get_obstacle', methods=['GET'])
@login_required
def get_obstacle():
    bbox = request.args.get('bbox', '40,-90,45,-85')
    data = get_obstacle_data(bbox=bbox)
    return jsonify(data)
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

