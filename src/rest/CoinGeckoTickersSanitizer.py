class TickersSanitizer():
    '''Reduces the dataset and provides default values for an incomming coin'''

    def __init__(self):
       pass

    def sanitize(self, exchangeData, symbol):
        '''Strips out unwanted data, creates a flat dict'''

        def get_prices(exchangeData):
            prices = []
            
            print('EXCHANGEDATA', exchangeData)
            if 'tickers' not in exchangeData or not exchangeData['tickers']:
                print(' 0, 0')
                return 0, 0

            tickers = exchangeData['tickers']
            print(len(tickers))
            for ticker in tickers:
                prices.append(ticker.get('converted_last', {}).get('usd', 0.0))
                print(ticker.get('converted_last', {}).get('usd', 0.0))
                print(prices)
                print(min(prices), max(prices))
            return min(prices), max(prices)

        minimum, maximum = get_prices(exchangeData)
        
        coinPricesHighLow = {}
        coinPricesHighLow['id'] = exchangeData['name']
        coinPricesHighLow['symbol'] = symbol
        coinPricesHighLow['highest_price'] = maximum
        coinPricesHighLow['lowest_price'] = minimum

        return coinPricesHighLow





