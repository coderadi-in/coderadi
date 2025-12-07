'''coderadi &bull; site core'''

# ? IMPORTING LIBRARIES
from flask import Flask
from extensions import *
import os

# ? IMPORTING ROUTES
from routers.router import router
from routers.api import api
from routers.services import services

# ! ───────────────────────────────┐
# ! LOADING VIRTUAL ENVIRONMENT    │
from dotenv import load_dotenv  #! │
load_dotenv('.venv/vars.env')   #! │
# ! ───────────────────────────────┘

# ! BUILDING SERVER
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
server.config['SQLALHCEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ! BINDING EXTENSIONS
db.init_app(server)

# ! INITIALIZING DATABASE
with server.app_context():
    db.create_all()

# ! BINDING ROUTER
server.register_blueprint(router)
server.register_blueprint(api)
server.register_blueprint(services)