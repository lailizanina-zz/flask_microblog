#importing from the packdege app the variable app(in __init__).
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

#this function is a call back to the event in which the function is associated to the URL / and /index.
@app.route('/')
@app.route('/index')
def index():
#the dictionary mock object is created
    user = {'username': 'Victoria'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Max'},
            'body': 'The best way to predict the future is to invent it!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
#function to login, from the /login URL that creates the form and render it.
# The method allows the app to acept POST requests, that will return form data to the server
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
#precesses the data.
#If app sends GET it returns False. In the case,the function skips the if statment and render the last line template
#If app sends POST, returns True. Validating the process and allowing the sign in.
    if form.validate_on_submit():
#Flash interracts with the user(messages). Allows the user to notice if the action was sucessful.
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
#The user acess the page inside the own URL. The function instructs the client web browser to automatically navigate to a different page.
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)
#return a template filename and a variable list of template arguments and returns the same template.

#Fask intercept the URL, activate the function and return "Hello, world!" to the browser.

