from dao.book import BookDAO


class BookService:

    def __init__(self, dao: BookDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        bid = data.get("id")
        author = self.get_one(bid)

        author.name = data.get("name")
        author.year = data.get("year")

        self.dao.update(author)

    def update_partial(self, data):
        bid = data.get("id")
        author = self.get_one(bid)

        if "name" in data:
            author.name = data.get("name")
        if "year" in data:
            author.year = data.get("year")

        self.dao.update(author)

    def delete(self, bid):
        pass
