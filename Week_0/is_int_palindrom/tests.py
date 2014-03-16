import unittest
from solution import is_int_palindrom


class IsIntPalindrom(unittest.TestCase):
    """docstring for IsIntPalindrom"""
    def test_is_int_palindrom(self):
        self.assertTrue(is_int_palindrom(1))
        self.assertTrue(not is_int_palindrom(42))
        self.assertTrue(is_int_palindrom(100001))
        self.assertTrue(is_int_palindrom(999))
        self.assertTrue(not is_int_palindrom(123))


if __name__ == '__main__':
    unittest.main()
