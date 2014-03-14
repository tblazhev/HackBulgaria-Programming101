import unittest
from solution import nth_fibonacci


class FibonacciTest(unittest.TestCase):
    """docstring for FibonacciTest"""
    def test_fibonacci(self):
        self.assertEqual(354224848179261915075, nth_fibonacci(100))
        self.assertEqual(1, nth_fibonacci(2))

if __name__ == '__main__':
    unittest.main()
