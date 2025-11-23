'''coderadi &bull; API structure for the project'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, request
from extensions import db, Project
import os

# ! BUILDING API ROUTER
api = Blueprint('api', __name__, url_prefix='/api')

# * FUNCTION TO CHECK ADMIN AUTHENTICATION
def check_admin_auth(passkey: str) -> bool:
    server_passkey = os.getenv('ADMIN_PASS')

    if (passkey == server_passkey):
        return True
    
    return False

# & DB-PROJECT `LIST` ROUTE
@api.route('/db/projects/list', methods=['GET'])
def get_db_list():
    '''Get the list of projects from db'''
    projects = Project.query.all()

    return {
        'res': {
            'status': 200,
            'message': 'Projects fetched successfully',
        },
        'data': [project.to_dict() for project in projects]
    }, 200

# & DB-PROJECT `NEW` ROUTE
@api.route('/db/projects/new', methods=['POST'])
def new_db_project():
    '''Create a new project in db'''

    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return {
            'res': {
                'status': 415,
                'message': 'Unsupported Media Type: Content-Type must be application/json',
            }
        }, 415
    
    passkey = request.headers.get('Admin-Key')    
    if (not check_admin_auth(passkey)):
        return {
            'res': {
                'status': 403,
                'message': 'Forbidden: Invalid Admin Key',
            }
        }, 403
    
    data = request.json
    new_project = Project(
        id=data.get('id'),
        cover=data.get('cover'),
        title=data.get('title'),
        desc=data.get('desc'),
        category=data.get('category'),
        pre_release=data.get('pre_release', False),
        external=data.get('external', False),
        tech_stack=data.get('tech_stack'),
        link=data.get('link')
    )

    try:
        db.session.add(new_project)
        db.session.commit()

        return {
            'res': {
                'status': 200,
                'message': 'Project created successfully!',
            }
        }, 200
    
    except Exception as e:
        db.session.rollback()
        return {
            'res': {
                'status': 500,
                'message': f'Internal Server Error: {str(e)}',
            }
        }, 500