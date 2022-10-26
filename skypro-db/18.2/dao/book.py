from dao.model.book import Book


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

    def update(self, data):
        bid = data.get("id")
        book = self.get_one(bid)

        book.name = data.get("name")
        book.year = data.get("year")

        self.session.add(book)
        self.session.comit()
        return book

    def update_partial(self, data):
        aid = data.get("id")
        book = self.get_one(aid)

        if "name" in data:
            book.name = data.get("name")
        if "year" in data:
            book.year = data.get("year")

        self.session.add(book)
        self.session.comit()
        return book

    def delete(self, aid):
        book = self.get_one(aid)
        self.session.delete(book)
        self.session.commit()
