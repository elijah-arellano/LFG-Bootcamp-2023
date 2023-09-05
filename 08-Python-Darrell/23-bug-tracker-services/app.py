
from flask import Flask, jsonify
from flask_restful import Api
from resources.bugs import Bugs
from resources.bug import Bug
from resources.projects import Projects
from resources.project import Project
from resources.users import UserRegister, UserLogin
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

from db import db

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/api_doc.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bug-tracker.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['BUNDLE_ERRORS'] = True #global setting for all the reqparsers in the app
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'lincoln'
jwt = JWTManager(app)

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity["is_admin"] == True:
        return { 'is_admin' : True }
    return { 'is_admin' : False }

@jwt.invalid_token_loader # we have to keep the argument here, since it's passed in by the caller internally
def invalid_token_callback(error):
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

#customizing the standard error when no token in the request

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description' : 'Request does not contain an access token',
        'error' : 'authorizatin_required'
    }), 401 




api.add_resource(Bugs, '/bugs')
api.add_resource(Bug, '/bugs/<int:id>')
api.add_resource(Projects, '/projects')
api.add_resource(Project, '/projects/<int:id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 8080, debug = True)


""" 
Header
    Authorization
    Bearer <access_token>

 """