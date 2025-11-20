'''coderadi &bull; site router'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, redirect, url_for, render_template, flash, request
from extensions import *

# ! BUILDING ROUTER
router = Blueprint('router', __name__)

# & BASE ROUTE
@router.route('/')
def home():
    flash("This site is under development, some functions may not work", "warning")
    return render_template('pages/home.html')

# & PROJECTS PAGE ROUTE
@router.route('/projects/')
def projects():
    flash("This site is under development, some functions may not work", "warning")
    return render_template('pages/projects.html')

# | SPECIFIC PROJECT ROUTE
@router.route('/projects/<project_id>')
def show_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    
    if (not project):
        flash("Project not found", "error")
        return redirect(url_for('router.projects'))
    
    if (not project.external):
        return render_template(project.link)
    
    return redirect(project.link)

# & ABOUT PAGE ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & CONTACT PAGE ROUTE
@router.route('/contact/')
def contact():
    return render_template('pages/contact.html')