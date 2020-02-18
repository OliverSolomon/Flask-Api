import os
import secrets
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp import db,app
from flaskapp.models import Blog, Notifications 
from flaskapp.master.forms import BlogForm
from flask_login import current_user,login_required



master = Blueprint('master',__name__)

def save_picture(form_image):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_image.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
	form_image.save(picture_path)
	return picture_fn

@master.route('/blog',methods=['POST','GET'])
#@login_required
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.image.data)
        post = Blog(title=form.title.data, content=form.content.data, image=picture_file, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created','success')
        return redirect(url_for('main.home'))
    return render_template('master/blog.html', form=form,title = 'Post_blog')


@master.route('/dashboard', methods=['POST','GET'])
#@login_required
def dashboard():
    notes = Notifications.query.all()
    return render_template('master/dashboard.html', title = 'Dashboard')

@master.route('/database', methods=['POST', 'GET'])
#@login_required
def database():
    return render_template('master/database.html', title='Database')


@master.route('/blog_tables', methods = ['POST','GET'])
#@login_required
def blog_tables():
    posts = Blog.query.all()
    return render_template ('master/blog_tables.html', posts=posts, title = 'Blogs')

