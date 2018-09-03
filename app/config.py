import os
basedir = os.path.abspath(os.path.dirname(__file__))

#Secret key is a crypthographic key to generate signatures/tokens and to protection against cross-site request forgery#
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# the variable defines were to get the data, in the case the URL data from dataenvironment variable. If it isn't defined, it takes basedir in the main directory application(app.db).
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
#disable the ALCHEMY configuration to sign the aplication every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#two expressions(a value sourced from an environment variable and a hardcored string, used in case the variable isn't disponible) joined by the or operator