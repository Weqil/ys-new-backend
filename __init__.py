from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)

#Прослушиваем файл роутов 
from routes.routes import *

if __name__ == "__main__":
    app.run(debug=True)
