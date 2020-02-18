from datetime import datetime
from flaskapp import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable = False)
  password = db.Column(db.String(60), nullable=False)
  is_admin = db.Column(db.Boolean, default=False)
  post = db.relationship('Blog', backref='author', lazy = True)

  def __repr__(self):
    return f"User('{self.username}')"
    

class Blog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable = False)
  image  = db.Column(db.String(120), nullable=False)
  date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
  content = db.Column(db.Text, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"Blog('{self.title}','{self.date_posted}','{self.content}')"

  
class Notifications(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40), nullable = True)
  date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
  email = db.Column(db.String(120), nullable = False)
  comments = db.Column(db.Text, nullable = False)

  def __repr__(self):
    return f"Blog('{self.name}','{self.date_posted}','{self.email}','{self.comments}')"