from flask import jsonify
from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt

from models.projects import ProjectModel
from resources.projects import new_project_parser

_project_parser = new_project_parser.copy()

_project_parser.add_argument('id',
                         type=int,
                         required=True,
                         help='Invalid data'
                         )
_project_parser.add_argument('created_at',
                         type=inputs.datetime_from_rfc822,
                             required=True,
                             help='Invalid data'
                             ) 

class Project(Resource):

    @jwt_required()
    def get(self, id):
        project_from_db = ProjectModel.get_by_id(id)  # data from db
        return jsonify(project_from_db.to_json())

    @jwt_required()
    def put(self, id):
        project_to_update = _project_parser.parse_args()  # data from user (postman)
        project_from_db = ProjectModel.get_by_id(id)  # data from db
        # updating the data from the db
        project_from_db.name = project_to_update['name']
        # updating the data from the db
        project_from_db.is_closed = project_to_update['is_closed']
        project_from_db.save()  # save the data back to the db
        return jsonify(project_from_db.to_json())

    @jwt_required()
    def delete(self, id):
        #get the user info from the claim
        """ 
        claims = get_jwt()
        if not claims['is_admin']:
            return {'message' : 'Admin privilege required'}, 401 
        """
        return f'Project-{id} will be removed'
