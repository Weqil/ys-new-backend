from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class Admin(db.Model):
      __tablename__ = 'admins'
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String(),nullable = False)
      password = Column(String(),nullable = False)
      films = relationship('films')