class BaseConfig:
    TESTING = False
    SECRET_KEY = "change me"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./bug-tracker.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = 'lincoln'
    pass

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True
    pass