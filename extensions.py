'''coderadi &bull; site extensions & database'''

# ? IMPORTING LIBRARIES
from flask_sqlalchemy import SQLAlchemy

# ! BUILDING EXTENSIONS
db = SQLAlchemy()

# | CONTACT DETAILS DATABASE MODEL
class ContactDetails(db.Model):
    '''
    ###### coderadi
    Holds the contact details filled by the user in contact form.

    ## Params
    - `id` [`primary_key`, `Integer`, `autoincrement`]: Id of row.
    - `name` [`String(50)`, `required`]: Name of user.
    - `email` [`String(75)`, `required`]: Email of user.
    - `subject` [`TEXT`]: Subject of contact.
    - `message` [`TEXT`]: Message from user.
    '''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False)
    subject = db.Column(db.TEXT)
    message = db.Column(db.TEXT, nullable=False)