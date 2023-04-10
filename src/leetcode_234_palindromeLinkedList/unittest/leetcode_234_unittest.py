import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_234_helper import LinkedList_Helper
from solutions.leetcode_234_brute_force import Solution as Solution1
from solutions.leetcode_234_optimized import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = LinkedList_Helper()
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        head = [1,2,2,1]
        expected_output = True

        actual_output = self.solution1.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        head = [1,2]
        expected_output = False

        actual_output = self.solution1.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        head = [1,2,3,2,1]
        expected_output = True

        actual_output = self.solution1.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        head = [1,2,3,4,2,1]
        expected_output = False

        actual_output = self.solution1.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_list(self):
        head = []
        expected_output = True

        actual_output = self.solution1.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.isPalindrome(head= self.helper.lst_to_linkedLst(head))
        self.assertEqual(actual_output, expected_output)




######################################
if __name__ == '__main__':
    unittest.main()