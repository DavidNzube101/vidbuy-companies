

from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(200), unique=True)
  password = db.Column(db.String(200))
  name = db.Column(db.String(200))
    