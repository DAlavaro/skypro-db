class PlayerRecords:
    @staticmethod
    def get_top_10():
        pass

    @staticmethod
    def get_top_100():
        pass

    @staticmethod
    def add_record(record):
        pass


top_10 = PlayerRecords.get_top_10()

class Cat:
    def say(self):
        self.what_does_cat_say()

    @staticmethod
    def what_does_cat_say():
        print("Meow")

Cat.what_does_cat_say()

cat = Cat()
cat.what_does_cat_say()

cat = Cat()
cat.say()