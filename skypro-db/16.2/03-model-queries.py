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

# Запросы данных
"""
SQL -> WHERE
query = User.query.filter(User.name == "Maxim")
"""
# query = db.session.query(User).filter(User.name == "Maxim")
# print(f'Запрос {query}')
# print(f'Результат: {query.first().name}')

"""
SQL -> WHERE (Рекомендуемы способ)
query = User.query.filter(User.name == "Maxim")
"""
# query = db.session.query(User).filter(User.name == "Maxim")
# print(f'Запрос {query}')
# print(f'Результат: {query.one()}')

"""
SQL -> WHERE ...AND
"""
# query = db.session.query(User).filter(User.id <= 5, User.age > 20)
# print(f'Запрос: {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> LIKE
"""
# query = db.session.query(User).filter(User.name.like("L%"))
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> WHERE ... OR
"""
# query = db.session.query(User).filter(
#     or_(User.id <= 5, User.age > 20)
# )
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> WHERE name IS NULL
"""
# query = db.session.query(User).filter(User.passport_number == None)
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> WHERE name NOT NULL
"""
# query = db.session.query(User).filter(User.passport_number != None)
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')


"""
SQL -> WHERE ... IN
"""
# query = db.session.query(User).filter(User.id.in_([1, 2]))
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> WHERE ... IN
"""
# query = db.session.query(User).filter(User.id.notin_([1, 2]))
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> WHERE ... BETWEEN
"""
# query = db.session.query(User).filter(User.id.between(1, 6))
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> LIMIT
"""
# query = db.session.query(User).limit(2)
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> offset
"""
# query = db.session.query(User).limit(2).offset(2)
# print(f'Запрос {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> OREDER BY
"""
# query = db.session.query(User).order_by(User.id)
# print(f'Запрос: {query}')
# print(f'Результат: {query.all()}')
# query = db.session.query(User).order_by(desc(User.id))
# print(f'Запрос: {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> INNER JOIN
"""
# query = db.session.query(User.name, Group.name).join(Group)
# print(f'Запрос: {query}')
# print(f'Результат: {query.all()}')

"""
SQL ->  LEFT JOIN
"""
# query = db.session.query(User.name, Group.name).join(Group, outer=True)
# print(f'Запрос: {query}')
# print(f'Результат: {query.all()}')

"""
SQL -> GROUP By (Scalar)
func -> count(user.id)
"""
# получаем количество пользователей по первой группе
# Запрашиваем функцию импортировав пакет func
# Делаем запрос колонки делаем join руппы и фильтроем по колонке Group.id по занченеию Group.id = 1
query = db.session.query(func.count(User.id)).join(Group).filter(Group.id == 1).group_by(Group.id)
print(f'Запрос: {query}')
print(f'Результат: {query.scalar()}')

exit()







if __name__ == '__main__':
    app.run(debug=True)