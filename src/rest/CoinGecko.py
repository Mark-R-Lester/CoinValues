'''Module message'''
from enum import Enum
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
        response = requests.get(CoinGeckoUrl.PING)
        return response.json()

    def get_coin_list(self):
        '''Method description'''
        response = requests.get(CoinGeckoUrl.COIN_LIST.value)
        return response.json()

    def get_full_coin(self, identifier):
        '''Gets the coin information from Coin Gecko for the coin identified by the identifer'''
        response = requests.get(CoinGeckoUrl.COIN.value % identifier)
        return response.json()

    def get_sanitized_coin(self, identifier):
        '''Method description'''
        fullCoin = self.get_full_coin(identifier)
        return CoinSanitizer().sanitize(fullCoin)

    def get_coin_tickers(self, identifier):
        '''Method description'''
        response = requests.get(CoinGeckoUrl.COIN_TICKERS.value % identifier)
        return response.json()

    def get_sanitized_coin_ticker(self, identifier, symbol):
        '''Method description'''
        tickers = self.get_coin_tickers(identifier)
        return TickersSanitizer(tickers, symbol)

    def get_coin_markets(self, identifier):
        '''Method description'''
        response = requests.get(CoinGeckoUrl.COIN_MARKETS.value % identifier)
        return response.json()

    def get_coin_market_chart(self, identifier):
        '''Method description'''
        response = requests.get(CoinGeckoUrl.COIN_MARKET_CHART.value % identifier)
        return response.json()

    def get_coin_market_chart_range(self, identifier):
        '''Method description'''
        response = requests.get(CoinGeckoUrl.COIN_MARKET_CHART_RANGE.value % identifier)
        return response.json()