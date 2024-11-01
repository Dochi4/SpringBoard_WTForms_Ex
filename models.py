"""Models for Adoption."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

default_img = "https://animalmicrochips.co.uk/images/default_no_animal.jpg"

class Pet(db.Model):
    """Pet Model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(50), 
                     nullable=False)
    
    species = db.Column(db.String(50),
                        nullable=False)
    
    photo_url = db.Column(db.String,
                          default=default_img)
 
    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, 
                          nullable=False,
                          default=True)

    def __repr__(self):
        return f"<Pet id={self.id}, name={self.name}, species={self.species}, age={self.age}, available={self.available}>"
