from flask import Flask
from flask_sqlalchemy import SQLAlchemy


""" создаем новое приложение с новым экземпляром фласка"""
app = Flask(__name__)

""" устанавливаем конфигурацию для подключения к базе данных """
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

""" создаем новый экземпляр SQLAlchemy и передаем туда наше приложение   """
db =SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)