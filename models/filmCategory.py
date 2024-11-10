from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class FilmCategory(db.Model):
      __tablename__ = 'filmCategory'
      id = Column(Integer, primary_key=True, index=True)
      film_id = Column(Integer,ForeignKey('films.id', ondelete = 'CASCADE'),nullable=False,)
      category_id = Column(Integer,ForeignKey('category.id'),nullable=False)