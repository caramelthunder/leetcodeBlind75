import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_621_solution import Solution

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        tasks, n = ["A","A","A","B","B","B"], 2
        expected_output = 8

        actual_ouput = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual_ouput, expected_output)
    
    def test_example_2(self):
        tasks, n = ["A","A","A","B","B","B"], 0
        expected_output = 6

        actual_ouput = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual_ouput, expected_output)

    def test_example_3(self):
        tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
        expected_output = 16

        actual_ouput = self.solution.leastInterval(tasks, n)
        self.assertEqual(actual_ouput, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()