import unittest
from solution import nth_fibonacci


class CountVowelsTest(unittest.TestCase):
    """docstring for CountVowelsTest"""
    def test_count_vowels(self):
        self.assertEqual(354224848179261915075, nth_fibonacci(100))
        self.assertEqual(1, nth_fibonacci(2))

if __name__ == '__main__':
    unittest.main()
