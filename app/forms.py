from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#inside class,the filds are variables that receive class objects imported from FlaskForm. The first argument is the indentification for the variable followed by the opicional arguments. 
class LoginForm(FlaskForm):
#the validator makes possible to the user insert the data and the DataRequired obligates the imput of some argument 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
