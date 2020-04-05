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
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = "postgres://pmmonraehkxjak:dc4d72d600cbcdf2049172dae34acea86879c49f6149ac8a7d8c4acbb7eee6d3@ec2-54-159-112-44.compute-1.amazonaws.com:5432/dfpgqniavdb5hf"
db = SQLAlchemy(app)

from app import views  # nopep8
