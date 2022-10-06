'''Module message'''
from enum import Enum
from time import sleep

import requests
from src.rest.CoinGeckoCoinSanitizer import CoinSanitizer
from src.rest.CoinGeckoTickersSanitizer import TickersSanitizer

class CoinGeckoUrl(Enum):
    '''Class description'''
    COIN_LIST = 'https://api.coingecko.com/api/v3/coins/list'
    PING = 'https://api.coingecko.com/api/v3/ping'
    COIN = 'https://api.coingecko.com/api/v3/coins/%s'
    COIN_ALL_DATA = 'https://api.coingecko.com/api/v3/coins/%s?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true'
    COIN_TICKERS = 'https://api.coingecko.com/api/v3/coins/%s/tickers'
    COIN_MARKETS = 'https://api.coingecko.com/api/v3/coins/markets'
    COIN_MARKET_CHART = 'https://api.coingecko.com/api/v3/coins/%s/market_chart'
    COIN_MARKET_CHART_RANGE = 'https://api.coingecko.com/api/v3/coins/%s/market_chart/range'
    


class CoinGecko:
    '''Class description'''

    def __init__(self):
        pass

    def ping(self):
        '''Method description'''
        return requests.get(CoinGeckoUrl.PING)
       
    def get_coin_list(self):
        '''Method description'''
        return self.__get(CoinGeckoUrl.COIN_LIST.value)

    def get_full_coin(self, identifier):
        '''Gets the coin information from Coin Gecko for the coin identified by the identifer'''
        return self.__get(CoinGeckoUrl.COIN.value % identifier)

    def get_sanitized_coin(self, identifier):
        '''Method description'''
        fullCoin = self.get_full_coin(identifier)
        return CoinSanitizer().sanitize(fullCoin)

    def get_coin_tickers(self, identifier):
        '''Method description'''
        return self.__get(CoinGeckoUrl.COIN_TICKERS.value % identifier)

    def get_sanitized_coin_ticker(self, identifier, symbol):
        '''Method description'''
        tickers = self.get_coin_tickers(identifier)
        return TickersSanitizer().sanitize(tickers, symbol)

    def get_coin_markets(self, identifier):
        '''Method description'''
        return self.__get(CoinGeckoUrl.COIN_MARKETS.value % identifier)

    def get_coin_market_chart(self, identifier):
        '''Method description'''
        return self.__get(CoinGeckoUrl.COIN_MARKET_CHART.value % identifier)

    def get_coin_market_chart_range(self, identifier):
        '''Method description'''
        return self.__get(CoinGeckoUrl.COIN_MARKET_CHART_RANGE.value % identifier)


    def __get(self, url):
        print('Calling :', url)
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print('Exception coin gecko time out sleeping for 1 minute')
                sleep(60)
            return self.__get_json_from_response(response)
        except:
            print('Exception: The response was: ', response)
            return {}
       
    def __get_json_from_response(self, response):
        try:
            return response.json()
        except:
            print('Exception: Could not get json from response: ', response)
            return {}