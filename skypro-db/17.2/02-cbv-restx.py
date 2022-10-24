from flask import Flask, request
from flask_restx import Api, Resource

# создаем Фласк указываем название приложения
app = Flask(__name__)

# создаем api которое является экземпляром класса API c аргументом приложения app
api = Api(app)

# регистрируем namespace
book_ns = api.namespace('')

books = [
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    {
        "id": 2,
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
]


@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        return books, 200

    def post(self):
        req_json = request.json
        books[len(books) + 1] = req_json
        return "", 201


@book_ns.route('/books/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204

if __name__ == '__main__':
    app.run(debug=False)