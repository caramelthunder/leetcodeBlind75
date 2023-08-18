import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_422_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertTrue(
            self.solution.validWordSquare(["abcd", "bnrt", "crmy", "dtye"])
        )

    def test_case_2(self):
        self.assertTrue(
            self.solution.validWordSquare(["abcd", "bnrt", "crm", "dt"])
        )

    def test_case_3(self):
        self.assertFalse(
            self.solution.validWordSquare(["ball", "asee", "let", "lep"])
        )

    def test_case_4(self):
        self.assertFalse(
            self.solution.validWordSquare(["ball", "aria", "leet", "lady"])
        )

    def test_case_5(self):
        self.assertTrue(self.solution.validWordSquare(["a"]))

    def test_case_6(self):
        self.assertTrue(self.solution.validWordSquare(["abc", "b", "c"]))


######################################
if __name__ == "__main__":
    unittest.main()
