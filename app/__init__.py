# creates the application object as an instance of class Flask.
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#upercase-class and lowercase-package/module
import logging
logger = logging.getLogger('flask_migrate')
handler = logging.StreamHandler()
logger.addHandler(handler)
#predefined variable that set the name of the module in the one which it is used.
app = Flask(__name__)
#telling flask to read and execute config
app.config.from_object(Config)
# objects that will represent the imported packedges
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

#the app variable is in the instance of class Flask __init__, inside the app packedge. 
from app import routes, models
