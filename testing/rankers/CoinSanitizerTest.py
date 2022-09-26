import unittest2

from src.persistence.JsonPersistence import JsonPersistence
from testing.TestData import TestData
from src.rest.CoinGeckoCoinSanitizer import CoinSanitizer

class CoinSanitizerTest(unittest2.TestCase):

    def test_sanitize(self):
        '''Sanitizes 10 coins wwhich sould then be in the format of the expected data'''
        
        fullCoinData = TestData().get_full_coin_data()
        expected = TestData().get_sanitized_coin_data()
        actual = []
        for fullCoin in fullCoinData:
            coin = CoinSanitizer().sanitize(fullCoin)
            actual.append(coin)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest2.main()