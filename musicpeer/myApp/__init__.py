from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating an application instance
app = Flask(__name__)
# adding the config file to the application
app.config.from_object(Config)
# creating a database instance
db = SQLAlchemy(app)
# creating a migration engine instance
migrate = Migrate(app, db)
# routes has all view functions; models help to define the structure of the database
from myApp import routes
