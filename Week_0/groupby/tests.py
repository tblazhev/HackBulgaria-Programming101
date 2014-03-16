import unittest
from solution import groupby


class GroupByTest(unittest.TestCase):
    """docstring for GroupByTest"""
    def test_groupby(self):
        res1 = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        res2 = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        res3 = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}

        self.assertEqual(res1, groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(res2, groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
        self.assertEqual(res3, groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

if __name__ == '__main__':
    unittest.main()
