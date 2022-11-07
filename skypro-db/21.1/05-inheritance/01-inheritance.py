


class Book:
    def __init__(self, name, pages, content, author):
        self.name = name
        self.pages = pages
        self.content = content
        self.author = author

class EBook(Book):
    def __init__(self, name, pages, content, author, links):
        super().__init__(name, pages, content, author)
        self.links = links


book_1 = Book("Книга Python", 300, "", "Я")
book_2 = EBook("Книга Python", 300, "", "Я", "https://library.io/book/006.pdf")
