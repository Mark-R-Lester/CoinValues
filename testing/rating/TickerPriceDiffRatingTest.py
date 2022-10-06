import unittest2

from src.rating.TickerPriceDiffRating import TickerPriceDiffRating
class TickerPriceDiffRatingTest(unittest2.TestCase):

    def setUp(self):
        self.ticker = {
                        'symbol': 'time', 
                        'highest_price': 140.1, 
                        'lowest_price': 10.98
                    }

    def test_non_zero_prices(self):
        expected = 92.16
        actual = TickerPriceDiffRating().add_rating(self.ticker)
        self.assertEqual(expected, actual['rating'] if actual else None)

    def test_lowest_price_is_zero(self):
        expected = None
        self.ticker['lowest_price'] =  0.0
        self.assertEqual(expected, None)

    def test_highest_price_is_zero(self):
        expected = None
        self.ticker['highest_price'] =  0.0
        self.assertEqual(expected, None)

if __name__ == '__main__':
    unittest2.main()