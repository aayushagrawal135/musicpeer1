from myApp import db
from datetime import datetime

# bseclass for all models is called .Model ; it is in the Flask instance
class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, primary_key=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_query = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    username = db.Column(db.Integer, db.ForeignKey('user.username'))

    def __repr__(self):
        return '<Query : {}>'.format(self.search_query)
