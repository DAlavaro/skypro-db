from flask import request
from flask_restx import Resource, Namespace

from dao.model.book import BookSchema

# Создаем наймспэйс
book_ns = Namespace('books')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

@book_ns.route('/' )
class BooksView(Resource):
    def get(self):
        all_books = book_dao.get_all()
        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        book_dao.get_all(req_json)
        return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):

    def get(self, aid: int):  # Получение данных
        one_authors =book_dao.get_one(aid)
        return book_schema.dump(one_authors), 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = aid
        book_dao.update(req_json)

        return "", 204

    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        book_dao.update_partial(req_json)

        return "", 204


    def delete(self, bid: int):
        book_dao.delete(bid)

        return "", 204
