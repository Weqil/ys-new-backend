from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class FilmCategory(db.Table):
      __tablename__ = 'filmCategory'
      film_id = Column(Integer,ForeignKey('films.id'),nullable=False)
      category_id = Column(Integer,ForeignKey('category.id'),nullable=False)