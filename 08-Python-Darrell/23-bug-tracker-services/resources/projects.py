from flask import  jsonify
from flask_restful import  Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.projects import ProjectModel

new_project_parser = reqparse.RequestParser()

new_project_parser.add_argument('title',
                             type=str,
                             help='Title cannot be blank',
                             required=True
                             )
new_project_parser.add_argument('desc',
                             type=str)
new_project_parser.add_argument('start_date',
                             type=inputs.date,
                             help='Start Date is required',
                             required=True
                             ) 



class Projects(Resource):

    @jwt_required()
    def get(self):  # <- will be invoked when a GET request is made for '/bugs'
        """ 
        identity = get_jwt_identity()
        print(identity) # => user id 
        """
        
        return jsonify([project.to_json() for project in ProjectModel.get_all()])

    @jwt_required()
    def post(self):
        new_bug = new_project_parser.parse_args()
        new_bug_model = ProjectModel(**new_bug)
        new_bug_model.save()
        return jsonify(new_bug_model.to_json())



