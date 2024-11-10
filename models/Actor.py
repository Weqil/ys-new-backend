from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import db
from sqlalchemy.orm import relationship
class Actor(db.Model):
      __tablename__ = 'actors'
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String(),nullable = False)
      description = Column(String(),nullable = False)
      date_spawn = Column(String(),nullable = False)
      film = relationship('filmActor')