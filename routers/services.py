'''coderadi &bull; services router'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, redirect, url_for, render_template, flash, request
from extensions import *

# ! BUILDING SERVICES ROUTER
services = Blueprint('services', __name__, url_prefix='/services')

# & SERVICES PAGE ROUTE
@services.route('/')
def services_page():
    flash("This site is under development, some functions may not work", "warning")
    return render_template('pages/services.html')

# & SPEICIFIC PROGRAM ROUTE
@services.route('/<program>/')
def show_program(program):
    return render_template(f'services/{program}.html')

# | POST ROUTE FOR `THE AUTHORITY LAUNCHPAD`
@services.route('/the-authority-launchpad/signup', methods=['POST'])
def signup_authority_launchpad():
    plan = request.form.get('plan')
    name = request.form.get('full-name')
    email = request.form.get('email')
    phone = request.form.get('phone', 'not-provided')

    new_application = TheAuthorityLaunchpad(
        plan=plan,
        name=name,
        email=email,
        phone=phone
    )

    db.session.add(new_application)
    db.session.commit()

    notify(f"""New application for `The Authority Launchpad | Fitness edition` is filled on your `portfolio` site.
Selected plan: {plan}
Name: {name}
Email: {email}
Phone: {phone}""")

    flash("Your application has been recorded. We'll get in touch within 24 hours.", "success")
    return redirect('/services/the-authority-launchpad/')