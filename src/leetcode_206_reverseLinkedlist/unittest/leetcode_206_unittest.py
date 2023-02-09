import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_206_iterative import Solution as Solution1
from solutions.leetcode_206_recursive import Solution as Solution2
from helpers.leetcode_206_helper import LinkedList_Helper

class Test(unittest.TestCase):
    def setUp(self):
        self.linkedList_helper = LinkedList_Helper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        
    
    def test_example_1(self):
        head = [1,2,3,4,5]
        expected_output = [5,4,3,2,1]

        actual_ouput1 = self.solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)
 
        actual_ouput2 = self.solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_example_2(self):
        head = [1,2]
        expected_output = [2,1]

        actual_ouput1 = self.solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)
 
        actual_ouput2 = self.solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_single_node(self):
        head = [1]
        expected_output = [1]

        actual_ouput1 = self.solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)
 
        actual_ouput2 = self.solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

    def test_empty_list(self):
        head = []
        expected_output = []

        actual_ouput1 = self.solution1.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput1), expected_output)
 
        actual_ouput2 = self.solution2.reverseList(self.linkedList_helper.list_to_linkedList(lst= head))
        self.assertEqual(self.linkedList_helper.linkedList_to_list(actual_ouput2), expected_output)

##########################################
if __name__ == '__main__':
    unittest.main()