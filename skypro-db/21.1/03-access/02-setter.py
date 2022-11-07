class User:
    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):
        self._name = new_name


user_1 = User("John")
user_1.set_name("Arthur")
