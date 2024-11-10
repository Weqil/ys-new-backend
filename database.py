from __init__ import app
from flask_sqlalchemy import SQLAlchemy
#Создаю класс базы данных что бы работать с ней
db = SQLAlchemy(app)
