"""Blogly application."""

from flask import Flask, request, render_template, redirect 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from sqlalchemy import text
from forms import PetForm

app = Flask(__name__)

# Configuration for the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True  
app.config["SECRET_KEY"] = "pet_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False  
connect_db(app)

# Initialize the database within the application context
with app.app_context():
    db.create_all()

debug = DebugToolbarExtension(app)

@app.route("/")
def list_page():
    """Shows list of pets from the database."""
    pets = Pet.query.all()  
   
    return render_template("home_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Render New Pet Form and Posts it"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data



        newpet = Pet(name = name,species =species , photo_url= photo_url,age=age,notes=notes, available= available)

        db.session.add(newpet)
        db.session.commit()
        return redirect("/")
    
    else:
     
     return render_template('add_pets.html' ,  form = form)
    
@app.route('/pet<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """Edit pet details based on ID."""

    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        
        return redirect("/")
    else:
     
     return render_template("edit_pet.html", form=form, pet=pet)
