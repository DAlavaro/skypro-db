class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, old_password, new_password): #public
        self._is_password_correct(old_password)
        self.__is_password_valid(new_password)
        self._was_password_used(new_password)

    def _is_password_correct(self, old_password): # protected
        """
        Проверяет пароль на корректность
        """
        pass

    def __is_password_valid(self, new_password): # private
        """
        Проверяет, что новый пароль подходит под требования безопасности
        """
        pass

    def _was_password_used(self, new_password):
        """
        Проверяет использовался ли этот пароль ранее
        """
        pass


user = User("John", "123123")
