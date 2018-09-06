#importing from the packdege app the variable app(in __init__).
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)