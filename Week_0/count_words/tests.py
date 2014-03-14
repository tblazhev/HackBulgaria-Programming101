import unittest
from solution import count_words


class CountVowelsTest(unittest.TestCase):
    """docstring for CountVowelsTest"""
    def test_count_vowels(self):
        res1 = {'banana': 1, 'pie': 1, 'apple': 2}
        res2 = {'python': 3, 'ruby': 1}

        self.assertEqual(res1, count_words(["apple", "banana", "apple", "pie"]))
        self.assertEqual(res2, count_words(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
    unittest.main()
