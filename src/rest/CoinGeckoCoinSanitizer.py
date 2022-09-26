class CoinSanitizer():
    '''Provides coin ranking for the main coin stream'''

    def __init__(self):
        self.args = [
            {'default': '', 'key': 'id', 'keys':['id']},
            {'default': '', 'key': 'symbol', 'keys':['symbol']},
            {'default': '', 'key': 'genesisDate', 'keys':['genesisDate']},
            {'default': '', 'key': 'coinGecko_score', 'keys':['coinGecko_score']},
            {'default': '', 'key': 'developer_score', 'keys':['developer_score']},
            {'default': '', 'key': 'liquidity_score', 'keys':['liquidity_score']},
            {'default': '', 'key': 'public_interest_score', 'keys': ['public_interest_score']},
            {'default': '', 'key': 'total_value_locked', 'keys':['market_data', 'total_value_locked']},
            {'default': '', 'key': 'mcap_to_tvl_ratio', 'keys':['market_data', 'mcap_to_tvl_ratio']},
            {'default': '', 'key': 'fdv_to_tvl_ratio', 'keys':['market_data', 'fdv_to_tvl_ratio']},
            {'default': '', 'key': 'current_price', 'keys':['market_data', 'current_price', 'usd']},
            {'default': '', 'key': 'ath', 'keys':['market_data', 'ath', 'usd']},
            {'default': '', 'key': 'ath_change_percentage', 'keys':['market_data', 'ath_change_percentage', 'usd']},
            {'default': '', 'key': 'ath_date', 'keys':['market_data', 'ath_date', 'usd']},
            {'default': '', 'key': 'atl', 'keys':['market_data', 'atl', 'usd']},
            {'default': '', 'key': 'atl_date', 'keys':['market_data', 'atl_date', 'usd']},
            {'default': '', 'key': 'market_cap', 'keys':['market_data', 'market_cap', 'usd']},
            {'default': '', 'key': 'fully_diluted_valuation', 'keys':['market_data', 'fully_diluted_valuation', 'usd']}
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



