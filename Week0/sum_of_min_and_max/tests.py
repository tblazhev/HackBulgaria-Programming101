import unittest
from solution import sum_of_min_and_max


class SumOfMinAndMaxTest(unittest.TestCase):
    def test_sum_of_min_and_max(self):
        self.assertEqual(4, sum_of_min_and_max([1, 2, 3]))
        self.assertEqual(90, sum_of_min_and_max([-10, 5, 10, 100]))

if __name__ == '__main__':
    unittest.main()
