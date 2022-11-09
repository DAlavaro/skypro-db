

class Grade:
    def __init__(self, value=0):
        self._value = value

    def __repr__(self):
        return f'Оценка: {self._value}'

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        return self._value == other.value

    def __gt__(self, other):
        return self._value > other.value

grade_1 = Grade(2)
grade_2 = Grade(3)
print(grade_1 < grade_2)



