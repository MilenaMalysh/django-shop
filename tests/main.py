import os
import sys
import unittest
from pathlib import Path

from shop.tests.basket_test import BasketTest


def test_main(args):
    a = BasketTest()
    test_modules = Path('.').glob('*_test.py')
    result_suite = unittest.TestSuite()

    for t in test_modules:
        try:
            mod = __import__(('.'.join(os.getcwd().split('\\')[-2:]) + '.' + str(t)[:-3]), globals(),
                             locals(), ['suite'])
            suits = getattr(mod, 'suite')
            result_suite.addTest(suits())
        except (ImportError, AttributeError):
            return 1
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(result_suite)


if __name__ == '__main__':
    sys.exit(test_main(sys.argv))