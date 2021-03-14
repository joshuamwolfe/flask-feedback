"""Models for Feedback app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = ""


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.string(30), nullable=False)

    def serialize(self):
        """Serialize User."""
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

    def __rep__(self):
        message = f"<User {self.id} email={self.email} first_name={self.first_name} last_name={self.last_name}>"
        return message


def connect_db(app):
    db.app = app
    db.init_app(app)

# TODO:

# username - a unique primary key that is no longer than 20 characters. --DONE
# password - a not-nullable column that is text --DONE
# email - a not-nullable column that is unique and no longer than 50 characters.--DONE
# first_name - a not-nullable column that is no longer than 30 characters.--DONE
# last_name - a not-nullable column that is no longer than 30 characters.--DONE