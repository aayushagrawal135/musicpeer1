from myApp import app
from flask import render_template, redirect, flash, request, url_for
from myApp.forms import LoginForm
from myApp.joinForm import SignupForm
import myApp.databaseAPIs as db

# URL and function mappings
@app.route('/')
@app.route('/index')
# This is a template for home page without sign in
def index():
    return render_template('index.html', title = 'Home', user = user)



@app.route("/login", methods=['GET', 'POST'])
def login(loggedin=False):
    form = LoginForm(request.form)
    if form.validate_on_submit() and db.properLogin(form):
        loggedin = True
        flash('Login requested for user {}'.format(form.email.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, loggedin= loggedin)



@app.route("/signup", methods=['GET', 'POST'])
def signup(joined=False):
    form = SignupForm(request.form)

    print(form.validate_on_submit())
    print(db.properSignup(form))
    print(form.password.data==form.re_password.data)

    if form.validate_on_submit():
        if form.password.data==form.re_password.data:
            joined = db.properSignup(form)
            if joined:
                print("joined")
                return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form, joined=joined)
