import unittest
from solution import goldbach


class GoldbachTest(unittest.TestCase):
    """docstring for GoldbachTest"""
    def test_goldbach(self):
        res1 = [(2, 2)]
        res2 = [(3, 3)]
        res3 = [(3, 5)]
        res4 = [(3, 7), (5, 5)]
        res5 = [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
        self.assertEqual(res1, goldbach(4))
        self.assertEqual(res2, goldbach(6))
        self.assertEqual(res3, goldbach(8))
        self.assertEqual(res4, goldbach(10))
        self.assertEqual(res5, goldbach(100))

if __name__ == '__main__':
    unittest.main()
