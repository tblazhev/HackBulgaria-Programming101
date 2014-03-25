import unittest
import os
from subprocess import check_output
import shutil


class ExtTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_dir_for_ext/"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        for i in range(3):
            filename = self.test_dir + "test" + str(i) + ".py"
            f = open(filename, "w")
            f.close()
        for i in range(4):
            filename = self.test_dir + "test" + str(i) + ".txt"
            f = open(filename, "w")
            f.close()
        for i in range(5):
            filename = self.test_dir + "test" + str(i) + ".fe"
            f = open(filename, "w")
            f.close()

    def test_ext_py(self):
        result = check_output("py ext.py py test_dir_for_ext/", shell=True)
        result = result.decode("UTF-8")
        self.assertEqual("3\n", result)

    def test_ext_txt(self):
        result = check_output("py ext.py txt test_dir_for_ext/", shell=True)
        result = result.decode("UTF-8")
        self.assertEqual("4\n", result)

    def test_ext_fe(self):
        result = check_output("py ext.py fe test_dir_for_ext/", shell=True)
        result = result.decode("UTF-8")
        self.assertEqual("5\n", result)

    def test_ext_none(self):
        result = check_output("py ext.py asdfas test_dir_for_ext/", shell=True)
        result = result.decode("UTF-8")
        self.assertEqual("0\n", result)

    def tearDown(self):
        shutil.rmtree(self.test_dir)


if __name__ == '__main__':
    unittest.main()
