from flask_wtf import FlaskForm 
from wtforms.fields.core import StringField 
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired



class shortLink(FlaskForm) :
    long_url = StringField("Blog Name",validators=[DataRequired()])
    submit = SubmitField("register",validators=[DataRequired()])
    
