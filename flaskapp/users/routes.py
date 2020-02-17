from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp import db, bcrypt
from flaskapp.models import User, Blog
from flaskapp.users.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users',__name__)

@users.route('/login', methods=['POST', 'GET'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.home'))
    else:
      flash('Login Unsuccessful','danger')
  return render_template('login.html', form=form,title = 'Login')

@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.home'))

@users.route('/register',methods=['POST', 'GET'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username = form.username.data, password= hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Registration succesfull','success')
    return redirect(url_for('users.login'))
  return render_template('admin/register.html', form=form,title = 'register')
