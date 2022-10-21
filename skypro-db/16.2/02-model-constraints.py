from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    passport_nomber = db.Column(db.String(3), unique=True) # Все значения в столбце должны быть уникальными
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

# """ удаляет все таблицы со всеми данными"""
# db.drop_all()

""" создаем все стаблицы """
db.create_all()

# # PK Unique exception
# """ Правило первичного ключа проверка на уникальность ключа """
# try:
#     """ Создаем пользователя """
#     user_01 = User(id=1, name="John", age=30, passport_nomber="123")
#
#     """ сохраняем пользователя """
#     with db.session.begin():
#         db.session.add(user_01)
#
#     """ создаем копию пользователя"""
#     user_01_copy = User(id=1, name="John", age=30, passport_nomber="465")
#
#     """ пытаемся сохранить нового пользователя"""
#     with db.session.begin():
#         db.session.add(user_01_copy)
#
# except Exception as e:
#     print(e)
#
#
# # Column Unique exception
# """ Проверка на уникальность колонки """
# try:
#     user_02 = User(id=2, name="Kate", age=30, passport_nomber="123")
#     with db.session.begin():
#         db.session.add(user_02)
# except Exception as e:
#     print(e)
#
# if __name__ == '__main__':
#     app.run(debug=True)


# # Check exception
# """ Проверка по ключу """
# try:
#     user_03 = User(id=3, name="Artur", age=15, passport_nomber="000")
#     with db.session.begin():
#         db.session.add(user_03)
# except Exception as e:
#     print(e)


# nullable exception
""" Проверка по ключу """
try:
    user_04 = User(id=4, name=None , age=25, passport_nomber="888")
    with db.session.begin():
        db.session.add(user_04)
except Exception as e:
    print(e)



if __name__ == '__main__':
    app.run(debug=True)