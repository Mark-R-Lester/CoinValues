import unittest2
from os.path import exists, getsize

from testing.TestData import TestData
from src.persistence.JsonPersistence import JsonPersistence

class JsonPersistenceTest(unittest2.TestCase):

    json = {"some": "json"}
    path = 'testing/testData/someJson.json'

    def setUp(self):
        fileExists = exists(self.path)
        if  fileExists:
            file = open(self.path, 'w')
            file.seek(0)
            file.truncate()
            file.close()
        else:
            file = open(self.path, 'w+')


    def test_environment(self):
        fileExists = exists(self.path)
        self.assertTrue(fileExists & getsize(self.path) == 0)


    def test_json_is_pesisted_read(self):
        persistence = JsonPersistence()
        persistence.persistJson(self.json, self.path)
        actual = persistence.loadJson(self.path)

        self.assertEqual(self.json, actual)
        

if __name__ == '__main__':
    unittest2.main()