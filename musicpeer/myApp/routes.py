from myApp import app
from flask import render_template, redirect, flash, request
from myApp.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aayush'}

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

    return render_template('index.html', title = 'Home', user = user, posts = posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
