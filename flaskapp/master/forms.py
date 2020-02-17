from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError



class BlogForm(FlaskForm):
    blog_title = StringField('Blog title', validators=[DataRequired()])
    blog_content = TextAreaField('Blog content', validators=[DataRequired()])
    submit = SubmitField('Post')