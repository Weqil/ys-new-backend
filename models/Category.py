from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class Category(db.Model):
      __tablename__ = 'category'
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String(),nullable = False)
      films = relationship('filmCategory')