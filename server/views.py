from flask import render_template, flash, request, redirect, url_for, send_from_directory
from server import app
from server import db
from server.models import User
from server.forms import LoginForm, RegistrationForm, AddRecordForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

import json
from scripts.statistics import get_data


###########
## PAGES ##
###########


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You're already logged in.")

        return redirect(url_for("admin"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("You've registered!")

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.")

        return redirect(url_for("admin"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username/password combination.")
            return redirect(url_for("login"))

        login_user(user)

        next_page = request.args.get("next")

        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("admin")

        return redirect(next_page)

    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()

    flash("Logged out successfully.")
    return redirect(url_for("index"))


@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")


# TODO: Implement proper actions
@app.route("/records", methods=["GET", "POST"])
def records():
    if not current_user.is_authenticated:
        flash("You need to be logged in to access this feature.")

        return redirect(url_for("login"))

    form = AddRecordForm()

    if form.validate_on_submit():
        flash("Record added!")

        return redirect(url_for("records"))

    return render_template("records.html", form=form)


@app.route("/stats")
def stats():
    return get_data()


##################
## STATIC FILES ##
##################


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


if __name__ == "__main__":
    app.run()
