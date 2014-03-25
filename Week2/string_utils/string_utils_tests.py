import string_utils
import unittest


class StringUtilsTest(unittest.TestCase):
    def test_lines(self):
        test_str = "line 1\nline 2\nline 3"
        expected = ["line 1", "line 2", "line 3"]
        self.assertEqual(expected, string_utils.lines(test_str))

    def test_unlines(self):
        expected = "line 1\nline 2\nline 3"
        test_list = ["line 1", "line 2", "line 3"]
        self.assertEqual(expected, string_utils.unlines(test_list))

    def test_words(self):
        test_text = "The quick brown fox jumped over the lazy dog"
        expected = ["The", "quick", "brown", "fox",
                    "jumped", "over", "the", "lazy", "dog"]
        self.assertEqual(expected, string_utils.words(test_text))
        test_text = "The quick brown fox\njumped over the lazy dog"
        expected = ["The", "quick", "brown", "fox",
                    "jumped", "over", "the", "lazy", "dog"]
        self.assertEqual(expected, string_utils.words(test_text))

    def test_unwords(self):
        expected = "The quick brown fox jumped over the lazy dog"
        test_words = ["The", "quick", "brown", "fox",
                      "jumped", "over", "the", "lazy", "dog"]
        self.assertEqual(expected, string_utils.unwords(test_words))

    def test_tabs_to_spaces(self):
        string = "this\tis\tstring example....wow!!!\t\tthis\tis really string"
        expected = "this is string example....wow!!!  this is really string"
        self.assertEqual(expected, string_utils.tabs_to_spaces(string, 1))
        self.assertEqual("", string_utils.tabs_to_spaces(""))


if __name__ == '__main__':
    unittest.main()
