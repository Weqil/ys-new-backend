from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class FilmActor(db.Model):
      __tablename__ = 'filmActor'
      id = Column(Integer, primary_key=True, index=True)
      film_id = Column(Integer,ForeignKey('films.id', ondelete = 'CASCADE'),nullable=False,)
      actor_id = Column(Integer,ForeignKey('actors.id', ondelete = 'CASCADE'),nullable=False)