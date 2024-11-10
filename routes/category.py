from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
import os
from controllers.CategoryController import CategoryController
from __init__ import app


@app.route('/category', methods = ['GET' , 'POST'])
def category():
        if request.method == 'POST':
            return CategoryController.createCategory()