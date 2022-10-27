from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired

class CreateRoster(FlaskForm):
    pokemon1 = StringField('Pokemon1', validators=[InputRequired()])
    pokemon2 = StringField('Pokemon2', validators=[InputRequired()])
    pokemon3 = StringField('Pokemon3', validators=[InputRequired()])
    pokemon4 = StringField('Pokemon4', validators=[InputRequired()])
    pokemon5 = StringField('Pokemon5', validators=[InputRequired()])
    pokemon6 = StringField('Pokemon6', validators=[InputRequired()])
    submit = SubmitField()