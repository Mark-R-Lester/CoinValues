
from threading import Thread
from time import sleep

from src.rest.CoinGecko import CoinGecko
from src.rating.FixedSupplyCoinRating import FixedSupplyCoinRating

class FixedSupplyCoinFeed:
    '''Class message'''

    def __init__(self):
        '''Constructor'''

    def feed(self):
        '''Fetches a coin listing iterates over all the coins and repeats the process indefinately'''
        while(True):
            coins = CoinGecko().get_coin_list()
            
            for coin in self.__feed(coins):
                if coin:
                    coins = []
                    coins.append(coin)
                    yield coins



    def __feed(self, coins):
        '''Fetches a sanitized coins one at a time, adds a rating to them 
        then yields them inside an array to the calling function'''
       
        for coin in coins:
            sanitizedCoin = CoinGecko().get_sanitized_coin(coin['id'])
            sanitizedCoin = FixedSupplyCoinRating().add_rating(sanitizedCoin)
            yield sanitizedCoin
            sleep(1.3)