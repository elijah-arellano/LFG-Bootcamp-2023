from flask import Flask, abort
from flask_restx import Api, Namespace, Resource, fields, reqparse
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix



app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)


app.config.from_object('server.config.DevelopmentConfig')

cors = CORS()
cors.init_app(app, resources={"*" : { "origins" : "*"}})


api = Api(app, version='1.0', title='User Management API', doc= "api/v1/register")
api.init_app(app)

# Namespace for user operations
user_ns = Namespace('users', description='User operations')

users = []


# Request parser for registration
registration_parser = reqparse.RequestParser()
registration_parser.add_argument('email', type=str, required=True, help='Email address')
registration_parser.add_argument('password', type=str, required=True, help='Password')
registration_parser.add_argument('confirm_password', type=str, required=True, help='Confirm Password')


# Model for user registration and user details
user_model = api.model('User', {
    'id': fields.Integer,
    'email': fields.String,
})


@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_with(user_model, as_list=True)
    def get(self):
        return users


@user_ns.route('/<int:user_id>')
class UserResource(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        user = next((u for u in users if u['id'] == user_id), None)
        if user is None:
            abort(404, 'User not found')
        return user


    def delete(self, user_id):
        user = next((u for u in users if u['id'] == user_id), None)
        if user is None:
            abort(404, 'User not found')
        users.remove(user)
        return {'message': 'User deleted successfully'}


@user_ns.route('/register')
class UserRegistration(Resource):
    @user_ns.expect(registration_parser)
    @user_ns.marshal_with(user_model)
    def post(self):
        args = registration_parser.parse_args()


        # Check if the email is already registered
        if any(user['email'] == args['email'] for user in users):
            abort(400, 'Email address is already registered')


        # Check if password and confirm_password match
        if args['password'] != args['confirm_password']:
            abort(400, 'Passwords do not match')


        # Create a new user
        user = {
            'id': len(users) + 1,
            'email': args['email'],
            'password_hash': password_hash,
        }
        users.append(user)


        return user, 201


@user_ns.route('/update/<int:user_id>')
class UserUpdate(Resource):
    @user_ns.expect(registration_parser)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        args = registration_parser.parse_args()


        # Find user by user_id
        user = next((u for u in users if u['id'] == user_id), None)
        if user is None:
            abort(404, 'User not found')


        # Check if email is already registered
        if any(u['email'] == args['email'] and u['id'] != user_id for u in users):
            abort(400, 'Email address is already registered by another user')


        # Check if password match
        if args['password'] != args['confirm_password']:
            abort(400, 'Passwords do not match')


        # Update the user's email and password
        user['email'] = args['email']
        user['password_hash'] = password_hash


        return user


if __name__ == '__main__':
    app.run(port = 8080,debug=True)





