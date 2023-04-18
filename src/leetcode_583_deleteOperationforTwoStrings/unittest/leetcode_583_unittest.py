import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_583_memoisation import Solution as Solution1
from solutions.leetcode_583_tabulation import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "word1": "sea", 
            "word2": "eat"
        }
        expected_output = 2

        actual_output = self.sol1.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minDistance(**params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = {
            "word1": "leetcode", 
            "word2": "etco"
        }
        expected_output = 4

        actual_output = self.sol1.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minDistance(**params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()