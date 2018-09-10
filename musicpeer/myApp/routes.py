from myApp import app
from flask import render_template, redirect, flash, request, url_for
from myApp.forms import LoginForm
from myApp.joinForm import SignupForm
from hashlib import sha256

# URL and function mappings
@app.route('/')
@app.route('/index')
# This is a template for home page without sign in
def index():
    user = {'username': ""}
    posts = [
    {
        'author' : {'username' : 'Ashutosh'},
        'body' : 'I am the best Quora celeb'
    },
    {
        'author' : {'username' : 'Aman'},
        'body' : 'Books > Movies'
    }
    ]

    return render_template('index.html', title = 'Home', user = user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit() and loginLogicCkeck(form):
        if form.remember_me.data == True:
            flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
        else:
            flash('Login requested for user {}'.format(form.email.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit() and signupLogicCheck(form):
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)
