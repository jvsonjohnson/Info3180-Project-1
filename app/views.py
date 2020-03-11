import os
from app import app
from . import db
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename


def format_date_joined():
    import datetime
    now = datetime.datetime.now()  # today's date
    date_joined = datetime.date(2019, 2, 7)  # a specific date
    return date_joined.strftime("%B, %Y")


class AddProfile(FlaskForm):
    fname = StringField("", validators=[DataRequired()])
    lname = StringField("", validators=[DataRequired()])
    gender = StringField("", validators=[DataRequired()])
    email = StringField("", validators=[DataRequired(), Email()])
    location = StringField("", validators=[DataRequired()])
    biography = StringField("", validators=[DataRequired()])
    photo = FileField(validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(120))
    biography = db.Column(db.String(140))
    photo = db.Column(db.String(255))

    def __init__(self, first_name, last_name, gender, email, location,
                 biography, photo):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/profile", methods=["POST", "GET"])
def profile():

    pform = AddProfile()

    if request.method == "POST" and pform.validate_on_submit():
        fname = pform.fname.data
        lname = pform.lname.data
        gender = pform.gender.data
        email = pform.email.data
        location = pform.location.data
        biography = pform.biography.data
        photo = pform.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        data = UserProfile(fname, lname, gender, email, location, biography,
                           filename)
        db.session.add(data)
        db.session.commit()
        flash("Profile was successfully added")
        return redirect(url_for('profiles'))

    return render_template("profile.html", form=pform)


@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    image_list = get_uploaded_images()
    return render_template("profiles.html",
                           users=users,
                           images=image_list,
                           date=format_date_joined())


@app.route("/profile/<userid>")
def userprofile(id):
    return UserProfile.query.get(int(id))


def get_uploaded_images():
    import os
    rootdir = os.getcwd()
    print(rootdir)
    ilist = []
    for subdir, dirs, files in os.walk(rootdir + r'\app\static\uploads'):
        for file in files:
            ilist.append(file)

    return ilist


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
