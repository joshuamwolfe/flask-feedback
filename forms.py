from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    """ register form """

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    first_name = StringField("first Name", validators=[InputRequired()])
    last_name = StringField("last Name", validators=[InputRequired()])


class LoginForm(FlaskForm):
    """login form"""

    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    """Add feedback form."""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Content",
        validators=[InputRequired()],
    )


class DeleteForm(FlaskForm):
    """Delete Form -- Intentionally left blank"""
