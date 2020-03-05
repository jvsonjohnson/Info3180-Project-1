from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


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


"""FINISH THIS FUNCTION"""


@app.route("/profile", methods=["POST", "GET"])
def profile():

    form = AddProfile()

    if request.method == "POST" and form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("Profile was successfully added")
        return redirect(url_for('profiles'))

    return render_template("profile.html", form=form)


@app.route("/profiles")
def profiles():
    return render_template("profiles.html", date=format_date_joined())


@app.route("/profile/<userid>")
def userprofile():
    return render_template("profiles.html", date=format_date_joined())


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