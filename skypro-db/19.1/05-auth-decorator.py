import jwt
from flask import request, abort, Flask
from flask_restx import Api, Resource

algo = 'HS256'
secret = 's3cR$eT'


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        # Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im15bmFtZSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNjY2MTIyODYwfQ.VlSYEsMRSPFinQywGqMJk4lLNWUGzOIq4v-8tdn13hw
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT Decode Excrption", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


app = Flask(__name__)
api = Api(app)
book_ns = api.namespace('')


@book_ns.route('/books')
class BooksView(Resource):

    def get(self):
        return [], 200

    @auth_required
    def post(self):
        return "", 201


if __name__ == '__main__':
    app.run(debug=False)

header payload signature