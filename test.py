import unittest2
from testing.rankers.MainCoinRankerTest import MainCoinRankerTest
from testing.rankers.CoinSanitizerTest import CoinSanitizerTest


if __name__ == "__main__":
    # suite = unittest2.defaultTestLoader.loadTestsFromTestCase(MainCoinRankerTest)
    # unittest2.TextTestRunner().run(suite)

    suite = unittest2.defaultTestLoader.loadTestsFromTestCase(CoinSanitizerTest)
    unittest2.TextTestRunner().run(suite)