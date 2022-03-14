from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import DataRequired
from ..models import Subscriber



class CommentForm(FlaskForm):
    user_comment = TextAreaField('comment on this Blog.')
    submit = SubmitField('Comment')

class BlogForm(FlaskForm):
    
    title = StringField('Blog title',validators=[DataRequired()])
    
    blog= TextAreaField('Enter Blog', validators=[DataRequired()])
    submit = SubmitField('Submit')
class SubscriberForm(FlaskForm):
    email = TextAreaField('enter your email address.',validators = [DataRequired()])
    username = TextAreaField('enter username', validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email = data_field.data).first():
            raise ValidationError('Your data already exists') 