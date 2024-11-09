from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for
from config.settings import settings

app = Flask(__name__)
#Подключаем наш конфиг в конфиг приложения
app.config.from_object(settings)

@app.route('/maksimmolodec',methods=("POST", "GET"))
def pizdec():
    if request.method == 'POST':
        return 'я обманул, максим пидор'
    return 'максим  молодец'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=settings.PORT)