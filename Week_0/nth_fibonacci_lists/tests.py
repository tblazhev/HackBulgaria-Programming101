import unittest
from solution import nth_fib_lists


class NthFibListsTest(unittest.TestCase):
    def test_nth_fib_lists(self):
        res1 = [3, 4, 1, 2, 3, 4]
        res2 = [1]
        res3 = [2]
        res4 = [1, 3, 1, 2]
        res5 = [1, 2, 3, 1, 2, 3]
        res6 = []

        self.assertEqual(res1, nth_fib_lists([1, 2], [3, 4], 4))
        self.assertEqual(res2, nth_fib_lists([1], [2], 1))
        self.assertEqual(res3, nth_fib_lists([1], [2], 2))
        self.assertEqual(res4, nth_fib_lists([1, 2], [1, 3], 3))
        self.assertEqual(res5, nth_fib_lists([], [1, 2, 3], 4))
        self.assertEqual(res6, nth_fib_lists([], [], 100))


if __name__ == '__main__':
    unittest.main()
