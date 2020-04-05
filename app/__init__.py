from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ENV = 'app'
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "staywoke"

if ENV == 'app':
    app.debug = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:project1@localhost/project1"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
db = SQLAlchemy(app)

from app import views  # nopep8
