from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "staywoke"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lab5:lab5@localhost/lab5"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
UPLOAD_FOLDER = './app/static/uploads'
from app import views  # nopep8
