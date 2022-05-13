import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = SECRET_KEY

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'token']

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES')))
