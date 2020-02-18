from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp import db, bcrypt
from flaskapp.models import User
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
      #login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('main.index'))
    else:
      flash('Login Unsuccessful','danger')
  return render_template('login.html', form=form,title = 'Login')

@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))

@users.route('/register',methods=['POST', 'GET'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username = form.username.data, password= hashed_password, is_admin = True)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('users.login'))
    flash('Registration succesfull','success')
  return render_template('master/register.html', form=form,title = 'register')


@users.route('/user_tables', methods = ['POST','GET'])
#@login_required
def user_tables():
    admins = User.query.all()
    return render_template ('master/user_tables.html', admins=admins, title = 'Users')
