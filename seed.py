from models import Pet, db
from app import app


with app.app_context():
    # drop and create table's info
    db.drop_all()
    db.create_all()

    # delete all entries in the Pet table, if any
    db.session.query(Pet).delete()

    # Test Users 
    whis = Pet(name='Whis',species='Dog',photo_url="https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", age = 2, notes = "Sure a good baby", available = True)
    vamp = Pet(name='Vamp',species='Cat', age = 4, notes = "Sure a good baby", available = False)
    tiggy = Pet(name='Tiggy',species='Tiger',photo_url="https://magazine.columbia.edu/sites/default/files/styles/facebook_sharing_1200x630/public/2022-08/Exp_tigers.jpg?itok=X2XGFDjQ", age = 200, notes = "Sure a good baby", available = True)

    # add test Users
    db.session.add_all([whis,vamp,tiggy])
    # commit test User
    db.session.commit()

    print("Database seeded!")