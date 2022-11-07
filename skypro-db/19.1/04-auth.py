from flask import request, abort, Flask
from flask_restx import Api, Resource


def login_required(func):
    def wrapper(*args, **kwargs):
        """
        Если слово authorisation не найдено в списке заголовков нашего реквеста
        тода мы прекращаем выполнение команды
        и отдаем код ошибки 401
        """
        if 'Authorisation' not in request.headers:
            abort(401)

        return func(*args, **kwargs)

    return wrapper


app = Flask(__name__)
api = Api(app)
# общий ns
book_ns = api.namespace('')


@book_ns.route('/books')
class BooksView(Resource):

    def get(self):
        return [], 200

    @login_required
    def post(self):
        return "", 201


if __name__ == '__main__':
    app.run(debug=False)

