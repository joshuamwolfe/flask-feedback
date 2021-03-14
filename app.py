from flask import Flask, url_for, render_template, redirect, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

# from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "abcdef"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

# TODO:

# Part 3: Make Routes For Users
# Make routes for the following:

# GET /
    # Redirect to /register.

# GET /register
    # Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name.
    # Make sure you are using WTForms and that your password input hides the characters that the user is typing!

# POST /register
    # Process the registration form by adding a new user. Then redirect to /secret

# GET /login
    # Show a form that when submitted will login a user. This form should accept a username and a password.
    # Make sure you are using WTForms and that your password input hides the characters that the user is typing!

# POST /login
    # Process the login form, ensuring the user is authenticated and going to /secret if so.

# GET /secret
    # Return the text “You made it!” (don’t worry, we’ll get rid of this soon)