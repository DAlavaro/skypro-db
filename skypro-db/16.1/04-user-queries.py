import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


""" создаем новое приложение с новым экземпляром фласка"""
app = Flask(__name__)

""" устанавливаем конфигурацию для подключения к базе данных """
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

""" создаем новый экземпляр SQLAlchemy и передаем туда наше приложение   """
db =SQLAlchemy(app)


""" Создаем класс User и наследуемся от базовой модели db.Model """
class User(db.Model):
    """ название таблицы """
    __tablename__ = "users"


    """  """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

""" удаляет все таблицы со всеми данными"""
db.drop_all()

""" создаем все стаблицы """
db.create_all()

""" Переменные класса User """
user_john = User(id=1, name="john", age=30)
user_kate = User(id=2, name="kate", age=31)

""" собираем список в одной переменной"""
users = [user_john, user_kate]
""" Добавляем весь список в таблицу """
db.session.add_all(users)

""" комит нашей сессии """
db.session.commit()


""" энд поинт который будет выдавать первого пользователя по адрес
    /users/first """
@app.route("/users/first")
def get_first_user():
    user = User.query.first()
    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


""" Энд поинт возвращающий общее количество пользователей int """
@app.route("/users/count")
def get_users_count():
    user_count = User.query.count()
    return json.dumps(user_count)

""" получает список из всех наших пользователей """
@app.route("/users")
def get_users():
    user_list = User.query.all() # ВЕРНЁТСЯ СПИСОК СУЩНОСТИ ВСЕХ ВОЗМОЖНЫХ ЗНАЧЕНИЙ
    user_response = []

    for user in user_list:
        user_response.append(
            {
                "id": user.id,
                "name": user.name,
                "age": user.age,
            }
        )
    return json.dumps(user_response)

""" Получение ответа по известного идентификатора и первичного ключу """
@app.route("/users/<int:sid>")
def get_user(sid: int):
    user = User.query.get(sid)

    if user is None:
        return "user not found"

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


if __name__ == '__main__':
    app.run(debug=True)