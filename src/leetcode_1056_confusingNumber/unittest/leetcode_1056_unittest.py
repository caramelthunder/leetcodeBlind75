import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1056_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.confusingNumber(6))

    def test_2(self):
        self.assertTrue(self.solution.confusingNumber(89))

    def test_3(self):
        self.assertFalse(self.solution.confusingNumber(11))

    def test_4(self):
        self.assertFalse(self.solution.confusingNumber(2))

    def test_5(self):
        self.assertFalse(self.solution.confusingNumber(25))

    def test_6(self):
        self.assertFalse(self.solution.confusingNumber(916))

    def test_7(self):
        self.assertTrue(self.solution.confusingNumber(160))


######################################
if __name__ == "__main__":
    unittest.main()
