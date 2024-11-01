from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField , IntegerField,SelectField
from wtforms.validators import InputRequired, Optional, URL,NumberRange

default_img = "https://animalmicrochips.co.uk/images/default_no_animal.jpg"

class PetForm(FlaskForm):
    """Add New Pet"""
    name = StringField("Pet's Name",
                        validators= [InputRequired(message="Please List Pet's name")])
    
    species= SelectField ("Pet's Species", 
                        choices=[("cat","Cat"),
                                 ('dog','Dog'),
                                 ('spike','Porcupine')],
                        validators= [InputRequired(message="Please List Pet's Species")])
    
    photo_url= StringField("Pet's Photo",
                        validators= [Optional(),URL(message="Please enter a valid URL.")] ,default=default_img,)
    
    age= IntegerField("Pet's Age",
                        validators= [Optional(),NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes= StringField("Pet Notes",
                        validators= [Optional()])
    available= BooleanField("Pet's Available", default=False)
   