from flask import request
from flask_restx import Resource, Namespace

from app.container import author_service
from app.dao.model.author import AuthorSchema

# Создаем наймспэйс
author_ns = Namespace('authors')

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

@author_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_authors = author_service.get_all()
        return authors_schema.dump(all_authors), 200

    def post(self):
        req_json = request.json
        author_service.get_all(req_json)
        return "", 201


@author_ns.route('/<int:bid>')
class AuthorView(Resource):

    def get(self, aid: int): # Получение данных
        one_authors = author_service.get_one(aid)
        return authors_schema.dump(one_authors), 200


    def put(self, aid):
        req_json = request.json
        req_json["id"] = aid
        author_service.update(req_json)

        return "", 204


    def patch(self, aid):
        req_json = request.json
        req_json["id"] = aid
        author_service.update_partial(req_json)

        return "", 204


    def delete(self, aid: int):
        author_service.delete(aid)

        return "", 204