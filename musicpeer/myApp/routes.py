from myApp import app
from flask import render_template
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
    form = LoginForm()

    if form.validate_on_submit():
        flash("login requested for user {} : remember -> {}".format(form.username.data, form.rememberMe.data))
        print("something is just here")
        return redirect("/index")

    return render_template("login.html", title = "Sign In", form = form)
