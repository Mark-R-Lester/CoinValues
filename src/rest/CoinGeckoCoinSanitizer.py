class CoinSanitizer():
    '''Reduces the dataset and provides default values for an incomming coin'''

    def __init__(self):
        self.args = [
            {'default': '', 'key': 'id', 'keys':['id']},
            {'default': '', 'key': 'symbol', 'keys':['symbol']},
            {'default': '', 'key': 'categories', 'keys':['categories']},
            {'default': 0.0, 'key': 'coinGecko_score', 'keys':['coinGecko_score']},
            {'default': 0.0, 'key': 'developer_score', 'keys':['developer_score']},
            {'default': 0.0, 'key': 'liquidity_score', 'keys':['liquidity_score']},
            {'default': 0.0, 'key': 'public_interest_score', 'keys': ['public_interest_score']},
            {'default': 0.0, 'key': 'total_value_locked', 'keys':['market_data', 'total_value_locked']},
            {'default': 0.0, 'key': 'mcap_to_tvl_ratio', 'keys':['market_data', 'mcap_to_tvl_ratio']},
            {'default': 0.0, 'key': 'fdv_to_tvl_ratio', 'keys':['market_data', 'fdv_to_tvl_ratio']},
            {'default': 0.0, 'key': 'current_price', 'keys':['market_data', 'current_price', 'usd']},
            {'default': 0.0, 'key': 'ath', 'keys':['market_data', 'ath', 'usd']},
            {'default': 0.0, 'key': 'ath_change_percentage', 'keys':['market_data', 'ath_change_percentage', 'usd']},
            {'default': 0.0, 'key': 'atl', 'keys':['market_data', 'atl', 'usd']},
            {'default': 0.0, 'key': 'market_cap', 'keys':['market_data', 'market_cap', 'usd']},
            {'default': 0.0, 'key': 'fully_diluted_valuation', 'keys':['market_data', 'fully_diluted_valuation', 'usd']},
            {'default': 0.0, 'key': 'max_supply', 'keys':['market_data', 'max_supply']},
            {'default': 0.0, 'key': 'total_supply', 'keys':['market_data', 'total_supply']},
            {'default': 0.0, 'key': 'circulating_supply', 'keys':['market_data', 'circulating_supply']},
            {'default': '1999-10-10T17:27:38.034Z', 'key': 'genesis_date', 'keys':['genesisDate']},
            {'default': '1999-10-10T17:27:38.034Z', 'key': 'ath_date', 'keys':['market_data', 'ath_date', 'usd']},
            {'default': '1999-10-10T17:27:38.034Z', 'key': 'atl_date', 'keys':['market_data', 'atl_date', 'usd']}
        ]

    def sanitize(self, coin):
        '''Strips out unwanted data'''
        sanitizedCoin = {}
        for arg in self.args:
            sanitizedCoin = self.__sanitizeField(coin, sanitizedCoin, arg)

        return sanitizedCoin


    def __sanitizeField(self, data, sanitizedCoin, arg):
        for key in arg['keys']:
            data = data.get(key, {})

        if data:
            sanitizedCoin[arg['key']] = data
        else:
            sanitizedCoin[arg['key']] = arg['default']

        return sanitizedCoin



