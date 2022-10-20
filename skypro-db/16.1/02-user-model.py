from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


""" создаем новое приложение с новым экземпляром фласка"""
app = Flask(__name__)

""" устанавливаем конфигурацию для подключения к базе данных """
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

""" создаем новый экземпляр SQLAlchemy и передаем туда наше приложение   """
db =SQLAlchemy(app)


""" Создаем класс User и наследуемся от базовой модели db.Model """
class User(db.Model):
    """ название таблицы """
    __tablename__ = "users"


    """  """
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)


""" создаем все стаблицы """
db.create_all()

""" Переменные класса User """
user_john = User(id=1, name="john", age=30)
user_kate = User(id=2, name="kate", age=31)

print(user_john, user_kate)

if __name__ == '__main__':
    app.run(debug=True)


