from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp.models import Blog


main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def index():
  blogs = Blog.query.all()
  return render_template('index.html', blogs=blogs,title = 'Blog')

@main.route('/terms')
def terms():
  return render_template ('terms.html', title = 'Terms and Conditions')
