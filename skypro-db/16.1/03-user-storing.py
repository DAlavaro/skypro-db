from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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



print(user_john, user_kate)

# """ добавление переменных в таблицу """
# db.session.add(user_john)
# db.session.add(user_kate)

""" собираем список в одной переменной"""
users = [user_john, user_kate]
""" Добавляем весь список в таблицу """
db.session.add_all(users)

print(db.session.new) # список не добавленных моделей

""" комит нашей сессии """
db.session.commit()

print(db.session.new) # список не добавленных моделей

if __name__ == '__main__':
    app.run(debug=True)


