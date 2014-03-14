import unittest
import os
from subprocess import call


class SpacifyTest(unittest.TestCase):
    def setUp(self):
        self.file_name = "temp_test"
        f = open(self.file_name, "w")
        self.tabs_string = "this is a\tstring with\t\tsome\ttabs\n"
        self.spaces_string = self.tabs_string.replace("\t", "    ")
        f.write(self.tabs_string)
        f.close()

    def test_spacify(self):
        call("py spacify.py " + self.file_name, shell=True)
        f = open(self.file_name, "r")
        contents = f.read()
        f.close()

        self.assertEqual(self.spaces_string, contents)

    def tearDown(self):
        os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
