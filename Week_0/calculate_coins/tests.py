import unittest
from solution import calculate_coins


class CalcCoinsTest(unittest.TestCase):
    """docstring for CalcCoinsTest"""
    def test_calc_coins(self):
        res1 = {1: 1, 50: 1, 20: 0, 5: 0, 100: 0, 10: 0, 2: 1}
        res2 = {1: 0, 50: 1, 20: 2, 5: 0, 100: 8, 10: 0, 2: 2}

        self.assertEqual(res1, calculate_coins(0.53))
        self.assertEqual(res2, calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()
