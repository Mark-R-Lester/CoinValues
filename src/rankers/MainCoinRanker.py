class MainCoinRanker():
    '''Provides coin ranking for the main coin stream'''

    def __init__(self):
        pass

    def rank(self, coins):
        '''Ranks the coins by:'''

        for coin in coins:
            print(coin['id'])
            print(coin['symbol'])

        return coins

   