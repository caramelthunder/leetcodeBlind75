import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_139_bottom_up_tabulation import Solution as Solution1
from solutions.leetcode_139_top_down_memoisation import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        params = (
            "leetcode",
            ["leet","code"]
        )
        expected_output = True

        actual_output = self.solution1.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = (
            "applepenapple",
            ["apple","pen"]
        )
        expected_output = True

        actual_output = self.solution1.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = (
            "catsandog",
            ["cats","dog","sand","and","cat"]
        )
        expected_output = False

        actual_output = self.solution1.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.wordBreak(*params)
        self.assertEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()