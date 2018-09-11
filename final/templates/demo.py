import pyrebase
from firebase_admin import db

config ={"apiKey": "AIzaSyDx254ID3TQXIZpp_Y-fU71O8xREOvwEhU", "authDomain": "musicpeer-bffc0.firebaseapp.com", "databaseURL": "https://musicpeer-bffc0.firebaseio.com", "projectId": "musicpeer-bffc0", "storageBucket": "musicpeer-bffc0.appspot.com", "serviceAccount": "/home/aayush/callOfDuty/musicpeer-bffc0-5dc52c0c048a.json"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("aayushagrawal135@gmail.com", "firebase")
#print(user['idToken'])

archer = {"name": "Sterling Archer", "agency": "Figgis"}
db.child("agents").push(archer, user['idToken'])
