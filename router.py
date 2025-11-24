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
    all_projects = Project.query.all()
    
    return render_template('pages/projects.html', data={
        'projects': all_projects
    })

# | SPECIFIC PROJECT ROUTE
@router.route('/projects/<project_id>')
def show_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    
    if (not project):
        flash("Project not found", "error")
        return redirect(url_for('router.projects'))
    
    if (not project.external):
        return render_template(f'{project.link}.html')
    
    return redirect(project.link)

# | SPECIFIC PROJECT ROUTE [DEV]
@router.route('/projects/dev/<project_id>')
def show_project_dev(project_id):
    return render_template(f'projects/{project_id}.html')

# & ABOUT PAGE ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & CONTACT PAGE ROUTE
@router.route('/contact/')
def contact():
    referral = request.args.get('ref')
    subject_referral = REFERRALS.get(referral, '')
    return render_template('pages/contact.html', subject_referral=subject_referral)