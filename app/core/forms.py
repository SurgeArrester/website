from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search_bar = StringField('Compound to Search', validators=[DataRequired()])
    results_to_display = StringField('Results', default='200', validators=[DataRequired()])
    must_contain = StringField('Must Contain', default='')
    must_exclude = StringField('Must Exclude', default='')
    search = SubmitField('Search')
