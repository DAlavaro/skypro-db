from dao.model.book import Book


# CRUD (Создание, чтение, обновление, удаление)
class AuthorDAO:
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
        author = self.get_one(bid)

        author.name = data.get("first_name")
        author.year = data.get("last_name")

        self.session.add(author)
        self.session.comit()
        return author

    def update_partial(self, data):
        aid = data.get("id")
        author = self.get_one(aid)

        if "first_name" in data:
            author.name = data.get("first_name")
        if "last_name" in data:
            author.year = data.get("last_name")

        self.session.add(author)
        self.session.comit()
        return author

    def delete(self, aid):
        author = self.get_one(aid)
        self.session.delete(author)
        self.session.commit()
