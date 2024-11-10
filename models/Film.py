
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class Film(db.Model):
      __tablename__ = 'films'
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String(128),nullable=False)
      description = Column(String,nullable=False)
      date_create = Column(String(128),nullable=False)
      country = Column(String(128),nullable=False)
      prewiev = Column(String(128),nullable=False)
      video = Column(String, nullable=False)
      user_create_id = Column(Integer,ForeignKey('admins.id'),nullable=False)
      actors = relationship('Actor', secondary='filmActor', back_populates='films')
      categories = relationship('Category', secondary='filmCategory', back_populates='films')