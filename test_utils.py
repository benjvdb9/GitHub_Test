# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(5), 120)
        self.assertEqual(utils.fact(3), 6)
        with self.assertRaises(ValueError):
            utils.fact(-5)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(9, 9, 9), (9, 9))
        self.assertEqual(utils.roots(0, 4, -16), (4))
        pass
    
    def test_integrate(self):
        self.assertEqual(utils.integrate(0, 4, 4), 8)
        self.assertEqual(utils.integrate(0, 2, 2), 2)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
