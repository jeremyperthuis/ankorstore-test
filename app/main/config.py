import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ankostore.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test-riseup-user.db')

config_by_name = dict(
    dev=DevelopmentConfig,
    testing=TestingConfig
)