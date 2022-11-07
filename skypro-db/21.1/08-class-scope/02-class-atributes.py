class Cat:
    color = "gray"
    bread = "default"
    name = "unknown"
    total_snacks = 0

    def __init__(self, name):
        self.name = name

    def add_snack(self):
        Cat.total_snacks += 1

    def get_snack(self):
        return Cat.total_snacks

    @classmethod
    def get_default_name(cls):
        return cls.name


cat_1 = Cat("Василий")
cat_1.add_snack()
cat_2 = Cat("Гошп")
cat_2.add_snack()
Cat.color = "red"

print(Cat.color)
print(Cat.bread)
print(Cat.name)

print(cat_1.color)
print(cat_1.bread)
print(cat_1.name)

print(cat_2.color)
print(cat_2.bread)
print(cat_2.name)

print(cat_1.get_snack())
print(Cat.total_snacks)
print(Cat.get_default_name())
