import unittest

from correct_price_test import ProductPriceTest
from product_addition_test import ProductAdditionTests


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ProductPriceTest))
    test_suite.addTest(unittest.makeSuite(ProductAdditionTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
