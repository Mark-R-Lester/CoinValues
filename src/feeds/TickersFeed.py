
from time import sleep

from src.rest.CoinGecko import CoinGecko
from src.rating.TickerPriceDiffRating import TickerPriceDiffRating

class TickersFeed:
    '''Class message'''

    def __init__(self):
        '''Constructor'''

    def feed(self):
        '''Fetches a coin listing iterates over all the coins and repeats the process indefinately'''

        def __feed(coins):
            '''Fetches sanitized tickers one at a time, adds a rating to them 
            then yields them inside an array to the calling function'''
        
            for coin in coins:
                id = coin['id']
                sanitizedTicker = CoinGecko().get_sanitized_coin_ticker(id, coin['symbol'])
                sanitizedTicker = TickerPriceDiffRating().add_rating(sanitizedTicker)
                yield sanitizedTicker
                sleep(5)

        while(True):
            coins = CoinGecko().get_coin_list()
            print('TICKERS fetch', len(coins))

            for coin in __feed(coins):
                print('TICKERS feed')
                if coin:
                    tickers = []
                    tickers.append(coin)
                    yield tickers

    