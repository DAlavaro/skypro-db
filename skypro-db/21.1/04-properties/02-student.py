


class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course


student = Student('John', 2)

student_name = student.name
student_course = student.course
