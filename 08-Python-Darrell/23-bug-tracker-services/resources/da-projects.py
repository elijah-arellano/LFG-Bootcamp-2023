from flask import jsonify
from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.projects import ProjectModel  # Assuming you have a ProjectModel class


new_project_parser = reqparse.RequestParser()

new_project_parser.add_argument('name',
                                type=str,
                                help='The field cannot be blank',
                                required=True
                                )
new_project_parser.add_argument('description',
                                type=str,
                                help='The field cannot be blank',
                                required=True
                                )



class Projects(Resource):
    # @jwt_required()
    def get(self):
        """
        identity = get_jwt_identity()
        print(identity) # => user id
        """
        return jsonify([project.to_json() for project in ProjectModel.get_all()])

    # @jwt_required()
    def post(self):
        new_project = new_project_parser.parse_args()
        new_project_model = ProjectModel(**new_project)
        new_project_model.save()
        return jsonify(new_project_model.to_json())
