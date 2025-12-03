'''coderadi &bull; API structure for the project'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, request
from extensions import db, Project, notify
import os, json

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
        'data': [{
            'id': project.id,
            'cover': project.cover,
            'title': project.title,
            'desc': project.desc,
            'category': project.category,
            'pre_release': project.pre_release,
            'external': project.external,
            'tech_stack': project.tech_stack,
            'url': project.url
        } for project in projects]
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
        url=data.get('url')
    )

    if (new_project.external):
        url_template = new_project.url
    else:
        url_template = f"https://coderadi.in/projects/{new_project.url}.html"

    try:
        db.session.add(new_project)
        db.session.commit()
        notify(f"New project added to `portfolio`.\n\n{url_template}\n\n    — coderadi.in")

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
    
# & DB-PROJECT `DELETE` ROUTE
@api.route('/db/projects/delete', methods=['DELETE'])
def delete_db_project():
    '''Delete a project from db'''

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
    project_id = data.get('id')

    project = Project.query.filter_by(id=project_id).first()
    if (not project):
        return {
            'res': {
                'status': 404,
                'message': 'Project not found',
            }
        }, 404

    try:
        db.session.delete(project)
        db.session.commit()
        notify(f"Project deleted from `portfolio`.\n\nID: {project_id}\n\n    — coderadi.in")

        return {
            'res': {
                'status': 200,
                'message': 'Project deleted successfully!',
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