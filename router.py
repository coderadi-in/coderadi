'''coderadi &bull; site router'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, redirect, url_for, render_template, flash, request

# ! BUILDING ROUTER
router = Blueprint('router', __name__)

# & BASE ROUTE
@router.route('/')
def home():
    return render_template('pages/home.html')

# & PROJECTS PAGE ROUTE
@router.route('/projects/')
def projects():
    return render_template('pages/projects.html')

# & ABOUT PAGE ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & CONTACT PAGE ROUTE
@router.route('/contact/')
def contact():
    return render_template('pages/contact.html')