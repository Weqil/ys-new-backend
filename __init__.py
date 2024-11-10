from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv, dotenv_values
from config import Config

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
#Прослушиваем файл роутов 
from routes.routes import *
from database import db
from models.Film import Film
from models.Admins import Admin
app.app_context().push()
if __name__ == "__main__":
    app.run(debug=True)

db.create_all()
