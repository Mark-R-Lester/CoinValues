import unittest2
from testing.rest.CoinSanitizerTest import CoinSanitizerTest
from testing.rest.TickersSanitizerTest import TickersSanitizerTest
from testing.persistence.JsonPersistenceTest import JsonPersistenceTest
from testing.rating.FixedSupplyCoinRatingTest import FixedSupplyCoinRatingTest
from testing.rating.TickerPriceDiffRatingTest import TickerPriceDiffRatingTest


if __name__ == "__main__":
  
    suite = unittest2.defaultTestLoader.loadTestsFromTestCase(TickerPriceDiffRatingTest)
    unittest2.TextTestRunner().run(suite)

    # suite = unittest2.defaultTestLoader.loadTestsFromTestCase(TickersSanitizerTest)
    # unittest2.TextTestRunner().run(suite)

    # suite = unittest2.defaultTestLoader.loadTestsFromTestCase(CoinSanitizerTest)
    # unittest2.TextTestRunner().run(suite)

    # suite = unittest2.defaultTestLoader.loadTestsFromTestCase(JsonPersistenceTest)
    # unittest2.TextTestRunner().run(suite)

    # suite = unittest2.defaultTestLoader.loadTestsFromTestCase(FixedSupplyCoinRatingTest)
    # unittest2.TextTestRunner().run(suite)
