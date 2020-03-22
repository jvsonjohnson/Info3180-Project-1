from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ENV = 'prod'
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "staywoke"

if ENV == 'dev':
    app.debug = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:project1@localhost/project1"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
else:
    app.debug = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = 'postgres://zeaoegrewvazmc:7231ed73a30674bfac050c92a92f079ae777a73ed3f27fdc4d26d6cfcd22b58b@ec2-3-91-112-166.compute-1.amazonaws.com:5432/da720bks2hm4ec'

db = SQLAlchemy(app)

from app import views  # nopep8
