from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskapp import db
from flaskapp.models import Notifications
#from flaskapp.master.forms import CommentForm
from flask_login import current_user,login_required


notifications = Blueprint('notifications',__name__)


@notifications.route('/comment_table', methods = ['POST','GET'])
#@login_required
def comment_table():
    notes = Notifications.query.all()
    return render_template ('master/comment_table.html', notes=notes, title = 'Notifications')