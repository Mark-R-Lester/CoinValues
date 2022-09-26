import unittest2

from testing.TestData import TestData
from src.rankers.MainCoinRanker import MainCoinRanker

class MainCoinRankerTest(unittest2.TestCase):

    def test_reduce(self):
        fullCoinData = TestData().get_full_coin_data()
        ranker = MainCoinRanker().rank(fullCoinData)

if __name__ == '__main__':
    unittest2.main()