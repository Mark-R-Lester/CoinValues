import unittest2
from testing.rest.CoinSanitizerTest import CoinSanitizerTest
from testing.persistence.JsonPersistenceTest import JsonPersistenceTest
from testing.rating.FixedSupplyCoinRatingTest import FixedSupplyCoinRatingTest


if __name__ == "__main__":
  
    suite = unittest2.defaultTestLoader.loadTestsFromTestCase(CoinSanitizerTest)
    unittest2.TextTestRunner().run(suite)

    suite = unittest2.defaultTestLoader.loadTestsFromTestCase(JsonPersistenceTest)
    unittest2.TextTestRunner().run(suite)

    suite = unittest2.defaultTestLoader.loadTestsFromTestCase(FixedSupplyCoinRatingTest)
    unittest2.TextTestRunner().run(suite)