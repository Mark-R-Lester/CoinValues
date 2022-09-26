
from src.persistence.JsonPersistence import JsonPersistence

class TestData():

    def __init__(self):
        pass

    def get_full_coin_data(self):
        return JsonPersistence().loadJson('testData/fullCoinData.json')

    def get_sanitized_coin_data(self):
        return JsonPersistence().loadJson('testData/sanitizedCoinData.json')

    
      
