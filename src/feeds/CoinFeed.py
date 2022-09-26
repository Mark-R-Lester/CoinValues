
from threading import Thread
from time import sleep

from ..rest.CoinGecko import CoinGecko

class CoinFeed:
    '''Class message'''

    def __init__(self):
        '''Constructor'''

    def feed(self):
        while(True):
            coins = CoinGecko().get_coin_list()
            for coin in self.__feed(coins):
                yield coin



    def __feed(self, coins):
        '''Anylyses the coins'''
        print(coins)
        for coin in coins:
            sanitizedCoins = []
            sanitizedCoin = CoinGecko().get_sanitized_coin(coin['id'])
            sanitizedCoins.append(sanitizedCoin)
            yield sanitizedCoins
            sleep(1.3)