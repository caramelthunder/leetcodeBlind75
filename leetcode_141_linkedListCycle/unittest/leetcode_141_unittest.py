import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_141_solution import Solution
from helpers.leetcode_141_helper import LinkedListHelper

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = LinkedListHelper()
        self.solution = Solution()

    def test_example_1(self):
        head = [3,2,0,-4]
        pos = 1
        expected_output = True
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        head = [1,2]
        pos = 0
        expected_output = True
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        head = [1]
        pos = -1
        expected_output = False
        actual_output = self.solution.hasCycle(self.helper.arr_to_list(head, pos))
        self.assertEqual(actual_output, expected_output)

########################################
if __name__ == '__main__':
    unittest.main()