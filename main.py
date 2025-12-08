'''coderadi &bull; site core'''

# ? IMPORTING LIBRARIES
from flask import Flask, render_template
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

# | ERROR HANDLERS

# & 404
@server.errorhandler(404)
def handle_404(error):
    return render_template('errors/404.html')

# & 500
@server.errorhandler(500)
def handle_500(error):
    return render_template('errors/500.html')