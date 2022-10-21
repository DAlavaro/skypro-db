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
    """ название таблицы """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
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

""" готовим группу новый объект класса Group """
group_01 = Group(id=1, name="Group #1")
""" создаем нового пользователя и прописываем группу объект класса Group """
user_01 = User(id=1, name="kate", age=31, group=group_01)

""" c помощью нового соединения записываем это в базу данных """
with db.session.begin():
    db.session.add(user_01)

""" создаем нового пользователя другим вариантом """
user_02 = User(id=2, name="Kate", age=31)
group_02 = Group(id=2, name="Group #2", users=[user_02])

with db.session.begin():
    db.session.add(group_02)

"""делаем селект чтобы вытащить информацию по id  """
user_with_group = User.query.get(2)
print(user_with_group.group.name)

if __name__ == '__main__':
    app.run(debug=True)