import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_19_two_passes import Solution as Naive
from solutions.leetcode_19_one_pass import Solution as Optimized
from helpers.leetcode_19_helper import LinkedListHelper

class Test(unittest.TestCase):

    def setUp(self):
        self.linkedListHelper = LinkedListHelper()
        self.naive_sol = Naive()
        self.optimized_sol = Optimized()

    def test_example_1(self):
        arr = [1,2,3,4,5]
        n = 2
        expected_output = [1,2,3,5]

        actual_output = self.naive_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

        actual_output = self.optimized_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

    def test_example_2(self):
        arr = [1]
        n = 1
        expected_output = []

        actual_output = self.naive_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

        actual_output = self.optimized_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

    def test_example_3(self):
        arr = [1,2]
        n = 1
        expected_output = [1]

        actual_output = self.naive_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

        actual_output = self.optimized_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)
    
    def test_example_4(self):
        arr = [1,2]
        n = 2
        expected_output = [2]

        actual_output = self.naive_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)

        actual_output = self.optimized_sol.removeNthFromEnd(head=self.linkedListHelper.arr_to_list(arr), n=n)
        self.assertEqual(self.linkedListHelper.list_to_arr(actual_output), expected_output)
######################################
if __name__ == '__main__':
    unittest.main()