from typing import Optional
from flask.app import Flask
from flask_wtf import *
from wtforms import *
from models import *
from wtforms.validators import *

class PetForm(FlaskForm):

    name = StringField("Pet Name",
                        validators=[InputRequired(message="Name cannot be blank")])
    
    species = SelectField("Species",
                        choices=[('fish', 'Fish'), ('dog', 'Dog'), ('hedgehog', 'Hedgehog')])

    photo_url = StringField("Photo Url",
                            validators=[URL(), Optional()])

    age = IntegerField("Pet Age",
                        validators=[Optional(), NumberRange(min=0, max=30)])
    
    notes = StringField("Notes")

    available = BooleanField("Is Available")