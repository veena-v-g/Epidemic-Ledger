from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from server.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()], render_kw={
        "placeholder": "Username",
        "class": "form-control"
    })

    password = PasswordField('Password', [DataRequired()], render_kw={
        "placeholder": "Password",
        "class": "form-control"
    })

    submit = SubmitField('Login', render_kw={
        "class": "btn btn-primary btn-lg btn-block"
    })


class RegistrationForm(FlaskForm):
    username = StringField("Username", [DataRequired()], render_kw={
        "placeholder": "Enter a username",
        "class": "form-control"
    })

    email = StringField("Email", [DataRequired(), Email()], render_kw={
        "placeholder": "Enter your email",
        "class": "form-control"
    })

    password = PasswordField("Password", [DataRequired()], render_kw={
        "placeholder": "Enter a password",
        "class": "form-control"
    })

    password_check = PasswordField("Verify Password", [DataRequired(), EqualTo("password")], render_kw={
        "placeholder": "Please re-enter your password",
        "class": "form-control"
    })

    submit = SubmitField("Register", render_kw={
        "class": "btn btn-primary btn-lg btn-block"
    })

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError("Username taken")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()

        if email is not None:
            raise ValidationError("Email address taken")


# TODO: Finish this
class AddRecordForm(FlaskForm):
    location = StringField("Location", [DataRequired()], render_kw={
        "placeholder": "Enter the location of the report",
        "class": "form-control"
    })

    date = StringField('Report Date', [DataRequired()], render_kw={
        "placeholder": "Enter the date of the report",
        "class": "form-control"
    })

    location_type = StringField('Location Type', [DataRequired()], render_kw={
        "placeholder": "What type of location data is it?",
        "class": "form-control"
    })

    data_field = StringField('Data Field', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    data_field_code = StringField('Data Field Code', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    time_period = StringField('Time Period', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    time_period_type = StringField('Time Period Type', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    value = StringField('Value', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    unit = StringField('Unit', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    geometry = StringField('Geometry', [DataRequired()], render_kw={
        "placeholder": "",
        "class": "form-control"
    })

    submit = SubmitField('Add Record', render_kw={
        "class": "btn btn-primary btn-lg btn-block"
    })
