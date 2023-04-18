import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_72_memoisation import Solution as Solution1
from solutions.leetcode_72_tabulation import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
        self.sol2 = Solution2()

    def test_example_1(self):
        params = {
            "word1": "horse", 
            "word2": "ros"
        }
        expected_output = 3

        actual_output = self.sol1.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minDistance(**params)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        params = {
            "word1": "intention", 
            "word2": "execution"
        }
        expected_output = 5

        actual_output = self.sol1.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        params = {
            "word1": "brainstorming", 
            "word2": "imagination"
        }
        expected_output = 9

        actual_output = self.sol1.minDistance(**params)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sol2.minDistance(**params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()