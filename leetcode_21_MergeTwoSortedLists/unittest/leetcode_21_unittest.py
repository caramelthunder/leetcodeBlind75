import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_21_iterative import Solution as Solution1
from solutions.leetcode_21_recursive import Solution as Solution2
from helpers.leetcode_21_helper import LinkedListHelper

class Test(unittest.TestCase):
    def setUp(self):
        self.s1 = Solution1()
        self.s2 = Solution2()
        self.helper = LinkedListHelper()
        
    def test_both_lists_not_empty(self):
        list1 = [1,2,4]
        list2 = [1,3,4]
        expected_output = [1,1,2,3,4,4]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))

        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
    def test_one_list_empty(self):
        list1 = []
        list2 = [1,3,4]
        expected_output = [1,3,4]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)

    def test_both_lists_empty(self):
        list1 = []
        list2 = []
        expected_output = []

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
    def test_one_list_single_element(self):
        list1 = [5]
        list2 = []
        expected_output = [5]

        solution1_ouput = self.helper.list_to_arr(self.s1.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
        solution2_ouput = self.helper.list_to_arr(self.s2.main(
            self.helper.arr_to_list(list1),
            self.helper.arr_to_list(list2)
            ))
            
        self.assertEqual(solution1_ouput, expected_output)
        self.assertEqual(solution2_ouput, expected_output)
    
##############################################
if __name__ == '__main__':
    unittest.main()
