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
    # MAIL SERVER SETTING (send you errors on email)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['golqeee13@gmail.com']