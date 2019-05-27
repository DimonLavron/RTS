from app import app, photos, db
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, PasswordField, FloatField, DateTimeField, TextAreaField, SelectField
from wtforms.validators import DataRequired, InputRequired, ValidationError

runners_col = db.runners

class RegisterRunnerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Register Runner')

    def validate_id(self, id):
        list = runners_col.distinct(key='id')
        if id.data in list:
            raise ValidationError('Please use a different id.')

class RegisterCheckpointForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Register Checkpoint')

class RegisterRaceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    logo = FileField('Logo', validators=[FileAllowed(photos, 'File is not an image.'), FileRequired('File was empty.')])
    admin = SelectField('Admin User', choices=[('admin', 'Admin'), ('organizer', 'Organizer')])
    laps_number = SelectField('Number of laps', coerce=int)
    distance = FloatField('Distance of the race (km)', validators=[InputRequired(), DataRequired('Not a right data format.')])
    date_and_time_of_race = DateTimeField('Date (Format: 01.01.2000 12:00)', format='%d.%m.%Y %H:%M', validators=[InputRequired(), DataRequired('Not a right data format.')])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Register Race')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
