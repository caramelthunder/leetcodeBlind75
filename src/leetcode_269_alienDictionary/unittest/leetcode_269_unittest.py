import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_269_breadth_first import Solution as Solution1
from solutions.leetcode_269_depth_first import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        words = ["wrt","wrf","er","ett","rftt"]
        expected_output = "wertf"

        actual_output = self.solution1.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)
        
        actual_output = self.solution2.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        words = ["z","x"]
        expected_output = "zx"

        actual_output = self.solution1.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)

    def test_example_3(self):
        words = ["z","x","z"]
        expected_output = ""

        actual_output = self.solution1.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_4(self):
        words = ["a","b","ca","cc"]
        expected_output = "abc"

        actual_output = self.solution1.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.alienOrder(words= words)
        self.assertEqual(actual_output, expected_output)
    
    
######################################
if __name__ == '__main__':
    unittest.main()