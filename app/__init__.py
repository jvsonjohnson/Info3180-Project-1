from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "staywoke"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:project1@localhost/project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/uploads'
from app import views  # nopep8
