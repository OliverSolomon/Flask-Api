from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp import db
from flaskapp.posts.forms import BlogForm
from flask_login import current_user,login_required
from flaskapp.models import Blog


posts = Blueprint('posts',__name__)


@posts.route('/blog',methods=['POST', 'GET'])
@login_required
def blog():
  if form.validate_on_submit():
    post = Blog(title=form.blog_title.data, content=form.blog_content.data, author = current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your post has been created','success')
    return redirect(url_for('home'))
  return render_template('admin/blog.html', form=form,title = 'Post_blog')