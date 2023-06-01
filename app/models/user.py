from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func, exists
from sqlalchemy.orm import column_property

class User(db.Model, UserMixin):
  __tablename__='users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(10), nullable=False)
  last_name = db.Column(db.String(10), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  hashed_password = db.Column(db.String(255), nullable=False)

  created_at = db.Column(db.DateTime(), nullable=False,server_default=func.now())
  updated_at = db.Column(db.DateTime(), nullable=False,onupdate=func.now(), default=func.now())

  @property
  def password(self):
    return self.hashed_password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def to_dict(self):
    return {
      'id': self.id,
      'first_name':self.first_name,
      'last_name':self.last_name,
      'email': self.email,
    }
