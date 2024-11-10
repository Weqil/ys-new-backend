from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
import os
from controllers.FilmController import FilmController
from __init__ import app

testFile = app
@app.route('/film', methods = ['GET' , 'POST'])
def film():
        if request.method == 'POST':
            return FilmController.createFilm()
        
