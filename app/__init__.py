# init is bones of application

from flask import Flask
# for the use config
from config import Config

#for sqlalchemy and migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'

# Database setting
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors