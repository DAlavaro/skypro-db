


class PrintedProduct:
    def __init__(self, name, pages, content):
        self.name = name
        self.pages = pages
        self.content = content


class Book(PrintedProduct):
    def __init__(self, name, pages, content, author):
        super().__init__(name, pages, content)
        self.author = author


class Magazine(PrintedProduct):
    def __init__(self, name, pages, content):
        super().__init__(name, pages, content)







