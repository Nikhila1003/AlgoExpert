import code
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = code.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
