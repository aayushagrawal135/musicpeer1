from myApp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aayush'}
    return render_template('index.html', user = user)
