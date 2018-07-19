import os

# configuration for bellow lines
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Config for secret key 
    # I use secret key for forms (csrf)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Configurations for database sqlite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False