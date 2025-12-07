"""coderadi &bull; site extensions & database"""

# ? IMPORTING LIBRARIES
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
import os

# ! BUILDING EXTENSIONS
db = SQLAlchemy()
client = Client(os.getenv("ACC_SID"), os.getenv("AUTH_TOKEN"))


# | CONTACT DETAILS DATABASE MODEL
class ContactDetails(db.Model):
    """
    ###### coderadi
    Holds the contact details filled by the user in contact form.

    ## Params
    - `id` [`primary_key`, `Integer`, `autoincrement`]: Id of row.
    - `name` [`String(50)`, `required`]: Name of user.
    - `email` [`String(75)`, `required`]: Email of user.
    - `subject` [`TEXT`]: Subject of contact.
    - `message` [`TEXT`]: Message from user.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False)
    subject = db.Column(db.TEXT)
    message = db.Column(db.TEXT, nullable=False)

# | PROJECT DETAILS DATABASE MODEL
class Project(db.Model):
    """
    ###### coderadi
    Holds the details of project built by coderadi.

    ## Params
    - `id` [`primary_key`, `Integer`]: Id of row.
    - `cover` [`String(100)`, `required`]: Cover image of project.
    - `title` [`String(100)`, `required`]: Title of project.
    - `desc` [`TEXT`, `required`]: Description of project.
    - `category` [`String(50)`, `required`]: Category of project.
    - `pre_release` [Boolean, `default=False`]: Is project pre-release.
    - `external` [Boolean, `default=False`]: Is project external.
    - `tech_stack` [`JSON`, `required`]: Technologies used in project.
    - `url` [`String(100)`]: path to the project.

    ### The `url` param
    If the project is external, means it's hosted outside coderadi's portfolio server, it'll host the complete URL to the project.
    Else, it'll host the relative path to the project on coderadi's server.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cover = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.TEXT, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    pre_release = db.Column(db.Boolean, default=False)
    tech_stack = db.Column(db.JSON, nullable=False)
    external = db.Column(db.Boolean, default=False)
    url = db.Column(db.String(100))

# | 'THE AUTHORITY LAUNCHPAD' SIGNUP DATABASE MODEL
class TheAuthorityLaunchpad(db.Model):
    """
    ###### coderadi
    Holds the details of signup froms filled by The Authority Launchpad users

    ## Params
    - `id`: [`primary_key`, `Integer`]: Id of row.
    - `plan`: [`String(10)`, `required`]: Selected plan.
    - `name`: [`String(50)`, `required`]: Name of applicant.
    - `email`: [`String(100)`, `required`]: Email of applicant.
    - `phone`: [`String(20)`]: Phone number of applicant.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))

# & DEFINING SOME CONSTANTS
REFERRALS = {
    "work": "I wanna work with you.",
    "connect": "I have a project to discuss with you.",
    "project": "I wanna build a project with you.",
}

# * FUNCTION TO SEND WHATSAPP NOTIFICATIONS
def notify(body: str):
    client.messages.create(
        body=body,
        from_=f"whatsapp:{os.getenv('FROM_NUMBER')}",
        to=f"whatsapp:{os.getenv('TO_NUMBER')}",
    )
