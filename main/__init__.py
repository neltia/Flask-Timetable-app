# flask packages
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import session
from flask import flash
# Database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Others
from datetime import datetime
import hashlib
import os


# app 객체 선언
app = Flask(__name__) 
salt = 'neltia' # secret key
now = str(datetime.now())
myHash = hashlib.sha512(str(now + salt).encode('utf-8')).hexdigest()
app.config['SECRET_KEY'] = myHash


# Firebase key
dbfile = '/main/static/dbkey.json'
cred = credentials.Certificate(os.getcwd() + dbfile)
firebase_admin.initialize_app(cred, {
  'projectId': 'neltia-manage'
})
db = firestore.client()


@app.route("/")
def index():
    return redirect(url_for("board.board_main"))


from . import board
from . import member


app.register_blueprint(board.blueprint)
app.register_blueprint(member.blueprint)
