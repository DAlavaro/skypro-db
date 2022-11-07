
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

    @course.setter
    def course(self, value):
        self._course = value

    @name.setter
    def name(self, value):
        self._name = value


student = Student('John', 2)

student_name = student.name
student_course = student.course

student.name = 'New name'
student.course = 1

print(student.name)
print(student.course)
