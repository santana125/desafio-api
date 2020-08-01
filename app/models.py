from sqlalchemy_serializer import SerializerMixin
from app.utils.database import db

class Planet(db.Model, SerializerMixin):
  __tablename__ = 'planets'
  serialize_only = ('id', 'name', 'climate', 'terrain', 'movies_appearances')
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=True)
  climate = db.Column(db.String(100), nullable=True)
  terrain = db.Column(db.String(100), nullable=True)
  movies_appearances = db.Column(db.Integer)
