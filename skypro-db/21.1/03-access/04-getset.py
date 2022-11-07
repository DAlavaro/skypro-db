class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


user_1 = User("John")
print(user_1.get_name())
user_1.set_name("Arthur")
print(user_1.get_name())