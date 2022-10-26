from flask import Flask
from flask_restx import Api

from app.views.authors import author_ns
from app.views.books import book_ns
from app.config import Config
from app.database import db
from app.dao.model.author import Author
from app.dao.model.book import Book


# Функция будет создавать приложение и возвращать его
def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    # задаем конфигурацию приложения вызвав специальный метод from_object
    application.config.from_object(config)
    # применяем конфигурацию чтобы фласк по всему приложению ее применил во все будущие компоненты
    application.app_context().push()

    return application


def configure_app(application: Flask):
    # обращаемся к базе данных и вызываем метод init_app
    db.init_app(application)
    api = Api(app)
    # вместо создания namespace реализуем добавление
    api.add_namespace(author_ns)
    api.add_namespace(book_ns)


def load_data():
    b1 = Book(id=1, name="Harry Potter", year=1992)
    b2 = Book(id=2, name="LE Comte dr Monte-Cristo", year=1854)

    a1 = Author(id=1, first_name="Joan", last_name="Routing")
    a2 = Author(id=2, first_name="Alexandre", last_name="Dumas")

    db.create_all()

    with db.session.begin():
        db.session.add_all([a1, a2])
        db.session.add_all([b1, b2])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run(debug=False)
