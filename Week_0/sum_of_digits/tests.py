import unittest
from solution import sum_of_digits


class SumOfDigitsTest(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(43, sum_of_digits(1325132435356))
        self.assertEqual(6, sum_of_digits(123))

if __name__ == '__main__':
    unittest.main()
