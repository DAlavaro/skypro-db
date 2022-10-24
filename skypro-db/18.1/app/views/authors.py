from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import AuthorSchema, Author

# Создаем наймспэйс
author_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

@author_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Author).all()
        return authors_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_user = Author(**req_json)

        with db.session.begin():
            db.session.add(new_user)
        return "", 201


@author_ns.route('/<int:bid>')
class BookView(Resource):

    def get(self, bid: int): # Получение данных
        try:
            book = db.session.query(Author).filter(Author.id == bid).one()
            return authors_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid):
        book = db.session.query(Author).get(bid)
        req_json = request.json

        book.name = req_json.get("name")
        book.year = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204

    def patch(self, bid):
        book = db.session.query(Author).get(bid)
        req_json = request.json

        if "name" in req_json:
            book.name = req_json.get("name")
        if "year" in req_json:
            book.age = req_json.get("year")

        db.session.add(book)
        db.session.commit()

        return "", 204


    def delete(self, bid: int):
        user = db.session.query(Author).get(bid)

        db.session.delete(user)
        db.session.commit()

        return "", 204