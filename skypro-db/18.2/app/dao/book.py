from app.dao.model.book import Book


# CRUD (Создание, чтение, обновление, удаление)
class BookDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        entity_list = self.session.query(Book).get(bid)
        return entity_list

    def get_all(self):
        entity_list = self.session.query(Book).all()
        return entity_list

    def create(self, data):
        book = Book(**data)
        self.session.add(book)
        self.session.commit()
        return book

    def update(self, book):
        self.session.add(book)
        self.session.comit()
        return book

    def delete(self, aid):
        book = self.get_one(aid)
        self.session.delete(book)
        self.session.commit()
