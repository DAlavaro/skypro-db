class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


user_1 = User("John")
print(user_1.get_name())


