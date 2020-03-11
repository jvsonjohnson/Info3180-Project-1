from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "staywoke"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "postgresql://spjefghktzbkvb:1edae354aab564d6349fcb9f10fc0e39c13997a65c4636ab2a0f6dfcaa0eb015@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d84e0e4finoaoo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from app import views  # nopep8
