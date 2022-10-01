class TickersSanitizer():
    '''Reduces the dataset and provides default values for an incomming coin'''

    def __init__(self):
        self.args = [
            {'default': '', 'key': 'symbol', 'keys':['symbol']},
            {'default': 0.0, 'key': 'highest_price', 'keys':['genesisDate']},
            {'default': 0.0, 'key': 'lowest_price', 'keys':['market_data', 'ath_date', 'usd']},
        ]

    def sanitize(self, tickers, symbol):
        '''Strips out unwanted data, creates a flat dict'''

        def get_prices(tickers):
            prices = []
            for ticker in tickers['tickers']:
                prices.append(ticker.get('converted_last', {}).get('usd', 0.0))
            return min(prices), max(prices)

        minimum, maximum = get_prices(tickers)
        
        coinPricesHighLow = {}
        coinPricesHighLow['symbol'] = symbol
        coinPricesHighLow['highest_price'] = maximum
        coinPricesHighLow['lowest_price'] = minimum

        return coinPricesHighLow





