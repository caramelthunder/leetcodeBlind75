import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_439_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.parseTernary("T?2:3"), "2")
        self.assertEqual(self.solution.parseTernary("F?1:T?4:5"), "4")
        self.assertEqual(self.solution.parseTernary("T?T?F:5:3"), "F")

    def test_nested(self):
        self.assertEqual(self.solution.parseTernary("T?T?T?1:2:3:4"), "1")
        self.assertEqual(self.solution.parseTernary("F?T?1:2:T?3:4"), "3")

    def test_edge(self):
        # Testing only conditions without '?'
        self.assertEqual(self.solution.parseTernary("TFT"), None)

        # Empty expression
        self.assertEqual(self.solution.parseTernary(""), None)

        # Single character
        self.assertEqual(self.solution.parseTernary("1"), "1")


######################################
if __name__ == "__main__":
    unittest.main()
