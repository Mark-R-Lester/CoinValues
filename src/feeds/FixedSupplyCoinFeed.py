
from tinydb import TinyDB, Query
from time import sleep

from src.rest.CoinGecko import CoinGecko
from src.rating.FixedSupplyCoinRating import FixedSupplyCoinRating


class FixedSupplyCoinFeed:
    '''Class message'''

    def __init__(self):
        '''Constructor'''
        db = TinyDB('database/coins.json')
        self.coinsTable = db.table('coins')
        self.lastSavedTable = db.table('lastSaved')
        self.coinQuery = Query()
        self.lastQuery = Query()


    def feed(self):
        '''Fetches a coin listing iterates over all the coins and repeats the process indefinately'''

        def __feed(coins):
            '''Fetches a sanitized coins one at a time, adds a rating to them 
            then yields them inside an array to the calling function'''
            for coin in coins:
                sanitizedCoin = CoinGecko().get_sanitized_coin(coin['id'])
                sanitizedCoin = FixedSupplyCoinRating().add_rating(sanitizedCoin)
                yield sanitizedCoin
                sleep(2.6)
       
        def convert(dbDict):
            '''Converts a the tinydb table to a standard dict'''
            dict = {}
            for key, value in dbDict.items():
                dict[key] = value
            return dict
        
        def removeTillLastSaved(coins, id):
            for coin in coins:
                if coin['id'] != id:
                    coins.remove(coin)
                else:
                    return

        for coin in self.coinsTable:
            coins = []
            coins.append(convert(coin))
            yield coins

        self.firstRun = True

        while(True):
            coins = CoinGecko().get_coin_list()

            if self.firstRun:
                lastSaved = self.lastSavedTable.search(self.lastQuery.coin == 'lastSaved')[0]
                id = convert(lastSaved)['id']
                removeTillLastSaved(coins, id)
                self.firstRun = False

            for coin in __feed(coins):
                if coin:
                    self.lastSavedTable.upsert({'coin': 'lastSaved', 'id': coin['id']}, self.lastQuery.coin == 'lastSaved')
                    self.coinsTable.upsert(coin, self.coinQuery.id == coin['id'])

                    coins = []
                    coins.append(coin)
                    yield coins

        
        
           
        
