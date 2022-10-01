
import dbm
from time import sleep

from src.rest.CoinGecko import CoinGecko
from src.rating.TickerPriceDiffRating import TickerPriceDiffRating

class TickersFeed:
    '''Class message'''

    def __init__(self):
        '''Constructor'''
        self.db = dbm.open('tickers','n')

    def feed(self):
        '''Fetches a coin listing iterates over all the coins and repeats the process indefinately'''
        while(True):
            coins = CoinGecko().get_coin_list()
            
            for coin in self.__feed(coins):
                if coin:
                    tickers = []
                    tickers.append(coin)
                    yield tickers

    def __feed(self, coins):
        '''Fetches sanitized tickers one at a time, adds a rating to them 
        then yields them inside an array to the calling function'''
       
        for coin in coins:
            id = coin['id']
            sanitizedTicker = CoinGecko().get_sanitized_coin_ticker(id)
            sanitizedTicker = TickerPriceDiffRating().add_rating(sanitizedTicker, coin['symbol'])
            self.db[id] = sanitizedTicker
            yield sanitizedTicker
            sleep(2.6)