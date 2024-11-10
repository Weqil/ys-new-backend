from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class FilmActor(db.Table):
      __tablename__ = 'filmActor'
      film_id = Column(Integer,ForeignKey('films.id'),nullable=False)
      actor_id = Column(Integer,ForeignKey('actors.id'),nullable=False)