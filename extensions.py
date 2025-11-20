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

# | PROJECT DETAILS DATABASE MODEL
class Project(db.Model):
    '''
    ###### coderadi
    Holds the details of project built by coderadi.

    ## Params
    - `id` [`primary_key`, `String(100)`]: Id of row.
    - `cover` [`String(100)`, `required`]: Cover image of project.
    - `title` [`String(100)`, `required`]: Title of project.
    - `desc` [`TEXT`, `required`]: Description of project.
    - `category` [`String(50)`, `required`]: Category of project.
    - `pre_release` [Boolean, `default=False`]: Is project pre-release.
    - `external` [Boolean, `default=False`]: Is project external.
    - `tech_stack` [`JSON`, `required`]: Technologies used in project.
    - `link` [`String(100)`]: Link to project.
    '''

    id = db.Column(db.String(100), primary_key=True)
    cover = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.TEXT, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    pre_release = db.Column(db.Boolean, default=False)
    external = db.Column(db.Boolean, default=False)
    tech_stack = db.Column(db.JSON, nullable=False)
    link = db.Column(db.String(100))