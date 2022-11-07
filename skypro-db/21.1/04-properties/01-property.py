class Cat:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


cat = Cat("Barsik")

name = cat.name

#cat.name() = "New name"

print(name)