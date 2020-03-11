from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = './app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "staywoke"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = 'postgresql://teglzpzzkxrkso:5857d0ccdeca10d6c08f2611a24d00ac76054a148ecfa6dc968b5d7b6a36337b@ec2-3-213-192-58.compute-1.amazonaws.com:5432/df29eckben8fnf'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from app import views  # nopep8
