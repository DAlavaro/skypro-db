from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

# создаем приложение фласк
app = Flask(__name__)
# настраиваем работу с базой данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

# создаем соединение с базой данных
db = SQLAlchemy(app)

# описываем нашу модель BOOK
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)

# готовим схему для сераилизации и дессереализации
class BookSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

# создаем объект API
api = Api(app)
# регистрируем namespace для работы с книгами
book_ns = api.namespace('')

b1 = Book(id=1, name="Гарри Поттер", author="Джоан Роулинг", year=1992)
b2 = Book(id=2, name="Граф Монте Кристо", author="Александр Дюма", year=1854)

# создаем таблицы
db.create_all()

# сохраняем книг в базу
with db.session.begin():
    db.session.add_all([b1, b2])

@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Book).all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Book(**req_json)
        with db.session.begin():
            db.session.add(new_book)
        return "", 201


@book_ns.route('/books/<int:bid>')
class BookView(Resource):

    def get(self, bid: int): # Получение данных
        try:
            book = db.session.query(Book).filter(Book.id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):     # обновление данных
        book = db.session.query(Book).get(bid)
        req_json = request.json

        book.name = req_json.get("name")
        book.author = req_json.get("author")
        book.year = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204

    def patch(self, bid):       # частичное обновление
        book = db.session.query(Book).get(bid)
        req_json = request.json

        if "name" in req_json:
            book.name = req_json.get("name")
        if "author" in req_json:
            book.author = req_json.get("author")
        if "year" in req_json:
            book.age = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204

# удаление данных
    def delete(self, bid: int):
        user = db.session.query(Book).get(bid)

        db.session.delete(user)
        db.session.commit()

        return "", 204

if __name__ == '__main__':
    app.run(debug=False)
