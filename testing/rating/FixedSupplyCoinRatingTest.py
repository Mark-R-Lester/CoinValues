import unittest2

from src.rating.FixedSupplyCoinRating import FixedSupplyCoinRating
from testing.TestData import TestData
from src.persistence.JsonPersistence import JsonPersistence

class FixedSupplyCoinRatingTest(unittest2.TestCase):

    def setUp(self):
        self.coin = {
                "circulating_supply": 10,
                "max_supply": 100,
                "ath": 1.0,
                "public_interest_score": 0.1,
                "current_price": 0.1,
                "ath_date": "2021-10-10T17:27:38.034Z"
            }

    def test_add_rating_max_supply_zero(self):
        self.coin['max_supply'] = 0.0
        self.__test(None)

    def test_add_rating_no_all_time_high(self):
        self.coin['ath'] = 0.0
        self.__test(None)

    def test_add_rating_all_time_high_too_early(self):
        self.coin['ath_date'] = "2020-10-10T17:27:38.034Z"
        self.__test(None)

    def test_add_rating_values_are_valid(self):
        self.__test(4000.0)

    def test_add_rating_circulating_supply_zero(self):
        self.coin['circulating_supply'] = 0.0
        self.__test(4.0)

    def test_add_rating_current_price_zero(self):
        self.coin['current_price'] = 0.0
        self.__test(400.0)

    def test_add_rating_public_interest_score_zero(self):
        self.coin['public_interest_score'] = 0.0
        self.__test(400.0)

    def __test(self, expected):
        actual = FixedSupplyCoinRating().add_rating(self.coin)
        self.assertEqual(expected, actual['rating'] if actual else None)

if __name__ == '__main__':
    unittest2.main()