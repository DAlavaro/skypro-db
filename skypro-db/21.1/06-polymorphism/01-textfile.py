import json


class TextFile:
    def read(self, file):
        with open(file) as f:
            return f.readlines()

    def write(self, file, lines):
        pass


class JsonFile:
    def read(self, file):
        with open(file) as f:
            return json.load(f)

    def write(self, file, lines):
        pass


file_processor = JsonFile()

data = file_processor.read('data.json')

print(data)