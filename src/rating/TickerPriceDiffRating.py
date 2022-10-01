
class TickerPriceDiffRating():
    '''Provides and percentage difference between the highest and lowset prices as a rating'''

    def __init__(self):
        pass

    def add_rating(self, ticker):
        '''Adds the rating or None is returned if the coin has a rating of zero'''

        rating = self.__get_rating(ticker)
        if rating:
            ticker['rating'] = rating
            return ticker
        else:
            return

    def __get_rating(self, ticker):
        min = ticker['lowest_price']
        max = ticker['highest_price']
        if min == 0 or max == 0:
            return
        return round(100 - ((max/100) * min), 2)