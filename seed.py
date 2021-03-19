from app import app
from models import connect_db, db, User, Feedback

db.drop_all()
db.create_all()

c1 = User(
    username="greenthingsjump",
    password="Carlmayer86",
    email="joshuamwolfe@gmail.com",
    first_name="Joshua",
    last_name="Wolfe",
)

c2 = User(
    username="er.boltsrock",
    password="Lightning05",
    email="er.boltsrock@gmail.com",
    first_name="Emily",
    last_name="Wolfe",
)

db.session.add_all([c1, c2])
db.session.commit()