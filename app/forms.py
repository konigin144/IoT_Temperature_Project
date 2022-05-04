from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import Optional

class SearchForm(FlaskForm):
    startdate = DateField('Start date', format='%Y-%m-%d', validators=[Optional()])
    starttime = TimeField('Start time', validators=[Optional()])
    enddate = DateField('End date', format='%Y-%m-%d', validators=[Optional()])
    endtime = TimeField('End time', validators=[Optional()])
    submit = SubmitField('Search')