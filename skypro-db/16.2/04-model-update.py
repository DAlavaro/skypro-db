from operator import or_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
from sqlalchemy.orm import relationship


""" создаем новое приложение с новым экземпляром фласка"""
app = Flask(__name__)
""" устанавливаем конфигурацию для подключения к базе данных """
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
""" создаем новый экземпляр SQLAlchemy и передаем туда наше приложение   """
db =SQLAlchemy(app)


""" Создаем класс User и наследуемся от базовой модели db.Model """
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(3), unique=True) # Все значения в столбце должны быть уникальными
    name = db.Column(db.String(100), nullable=False) # запрет на пустую строчку
    age = db.Column(db.Integer, db.CheckConstraint("age > 18")) # Ограничение на удовлетворения условия age > 18
    """ новая колонка с указанием внешнего ключа со ссылкой на таблицу group и столбик id  """
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = relationship("Group")

class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = relationship("User")

# Создаем все таблицы
db.create_all()

# Подготовка данных

group_01 = Group(id=1, name="Group #1")
group_02 = Group(id=2, name="Group #2")

user_01 = User(id=1, name="John", age=20, group=group_01)
user_02 = User(id=2, name="Kate", age=21, group=group_02)
user_03 = User(id=3, name="Artur", age=22, group=group_01)
user_04 = User(id=4, name="Maxim", age=23, group=group_01)
user_05 = User(id=5, name="Lily", age=24, group=group_02)
user_06 = User(id=6, name="Mary", age=25, group=group_02)

# При помощи сессии сохраняем все данные нам в таблицу
with db.session.begin():
    db.session.add_all([
        user_01,
        user_02,
        user_03,
        user_04,
        user_05,
        user_06,
    ])

# Запросы юзера по pk=2
user = User.query.get(2)
print(user.name)

user.name = "Update name"
print(user.name)

print(User.query.get(2))

db.session.add(user)
db.session.commit()
print(User.query.get(2))












if __name__ == '__main__':
    app.run(debug=True)