import json

class JsonPersistence():

    def __init__(self):
        pass

    def persistJson(self, dict, path):
        json.dump(dict, open(path, 'w+'))

    def loadJson(self, path):
        return json.load(open(path))