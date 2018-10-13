from flask import render_template, flash, redirect, \
    url_for
from server import app
from server.forms import LoginForm


@app.route("/")
def index():
    return "Home page"


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}")

        return redirect(url_for("index"))

    return render_template("login.html", form=form)
