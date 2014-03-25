import unittest
from solution import is_prime


class IsPrimeTest(unittest.TestCase):
    """docstring for IsPrimeTest"""
    def test_is_prime(self):
        self.assertTrue(not is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(not is_prime(8))
        self.assertTrue(is_prime(11))
        self.assertTrue(not is_prime(-10))


if __name__ == '__main__':
    unittest.main()
