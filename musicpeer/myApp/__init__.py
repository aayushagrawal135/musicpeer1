from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import myApp.modelSQL as sql

def createTables():
    conn, cursor = sql.open()
    sql.create_table_Users(cursor)

createTables()

# creating an application instance
app = Flask(__name__)
# adding the config file to the application
app.config.from_object(Config)
# routes has all view functions; models help to define the structure of the database
from myApp import routes
