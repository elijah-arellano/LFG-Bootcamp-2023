from flask_restful import Resource, reqparse
from model.users import UserModel
from flask_jwt_extended import create_access_token


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email', type=str, required=True,
                           help="This field cannot be blank")
_user_parser.add_argument('password', type=str, required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('confirm_password', type=str, required=True,
                          help="Confirm Password")

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return { 'message' : 'A user with that email already exists'}, 400
        
        user = UserModel(data['email'], data['password'])
        user.save_to_db()
        return {'message' : 'User created successfully'}, 201

class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if user and user.password == data['password']:
            access_token = create_access_token(identity={"email" : user.email, "is_admin" : True }, fresh=True)
            return { 'access_token' : access_token }

        return {'message' : 'Invalid Credentials'}, 401



class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message' : 'User not found'}, 404
        return user.json()