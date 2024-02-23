import unittest
import os


class TestCase(unittest.TestCase):

    def test_test(self):
        cwd = os.getcwd()
        print("!!!!!!!!!!!!???????????", cwd)


if __name__ == '__main__':
    unittest.main()
