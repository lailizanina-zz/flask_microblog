# creates the application object as an instance of class Flask.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
#upercase-class and lowercase-package/module

#predefined variable that set the name of the module in the one which it is used.
app = Flask(__name__)
#telling flask to read and execute config
app.config.from_object(Config)
# objects that will represent the imported packedges
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

#the app variable is in the instance of class Flask __init__, inside the app packedge. 
from app import routes, models