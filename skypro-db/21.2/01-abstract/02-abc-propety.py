from abc import ABC, abstractproperty, abstractmethod


class BaseCource(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def credits(self):
        pass


class Course(BaseCource):
    def __init__(self, title, description, credits):
        self._title = title
        self._description = description
        self._credits = credits

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def credits(self):
        return self._credits

course = Course('Title', 'Description', 15)

