import unittest2

from testing.TestData import TestData
from src.rest.CoinGeckoTickersSanitizer import TickersSanitizer


class TickersSanitizerTest(unittest2.TestCase):

    def test_sanitize(self):
        '''Sanitizes the ticker data for time and return the highest and lowest prices for symbol'''
        
        fullTickersData = TestData().get_full_tickers_data()
        expected = {'id': 'Wonderland', 'symbol': 'time', 'highest_price': 140.1, 'lowest_price': 10.98}
        actual = TickersSanitizer().sanitize(fullTickersData, 'time')

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest2.main()