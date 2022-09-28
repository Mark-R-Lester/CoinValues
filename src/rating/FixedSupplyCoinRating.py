import datetime
from pytz import UTC

from dateutil import parser 

class FixedSupplyCoinRating():
    '''Provides coin ranking for the main coin stream'''

    def __init__(self):
        pass

    def add_rating(self, coin):
        '''Gets the coin rating and adds it to the coin'''

        coin['rating'] = self.__get_rating(coin)
        return coin


    def __get_rating(self, coin):
        '''Ensures the coin can be rated.
           Returns None if the coin does not have the correct data for this rating
           Returns a calculated rating if the '''
        if self.is_coin_valid_for_rating(coin):
            return self.__calculate_rating(coin)

        return
        

    def is_coin_valid_for_rating(self, coin):
        '''Determines whether or the coin has all the required data to calculate a rating'''

        def has_max_supply(coin):
            return True if coin['max_supply'] else False

        def all_time_high_greater_than_zero(coin):
            return True if coin['ath'] else False
       
        def all_time_high_after_cutoff_date(coin):
            cutoff_date = datetime.datetime(2021, 1, 1)
            cutoff_date = UTC.localize(cutoff_date)
            all_time_high_date = parser.parse(coin['ath_date'])

            return all_time_high_date > cutoff_date

        if has_max_supply(coin) and all_time_high_after_cutoff_date(coin) and all_time_high_greater_than_zero(coin):
            return True
        return False


    def __calculate_rating(self, coin):
        '''Caculates the rating for this class'''

        def sanitize(value):
            return value if value else 0.01

        def total_supply_percentage(coin):
            '''Calculates the current supply as a percentage of the max supply'''
            circulating_supply = sanitize(coin['circulating_supply'])
            max_supply = coin['max_supply']
            return (100/max_supply) * circulating_supply

        def public_interest_percentage(coin):
            '''Converts public interest into a percentage'''
            public_interest_score = sanitize(coin['public_interest_score'])
            return public_interest_score * 100

        def percent_of_all_time_high(coin):
            '''Calculates the current price as a percentage of the all time high'''
            current_price = sanitize(coin['current_price'])
            ath = sanitize(coin['ath'])
            return (100/ath) * current_price

        return (total_supply_percentage(coin)*2) * ( public_interest_percentage(coin)*2) * percent_of_all_time_high(coin)