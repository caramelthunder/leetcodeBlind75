import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_232_helper import Helper

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
    
    def test_example_1(self):
        method_names = ["MyQueue", "push", "push", "peek", "pop", "empty"]
        params = [[], [1], [2], [], [], []]
        expected_output = [None, None, None, 1, 1, False]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_pushes(self):
        method_names = ["MyQueue", "push", "push", "push", "pop", "pop", "pop", "empty"]
        params = [[], [1], [2], [3], [], [], [], []]
        expected_output = [None, None, None, None, 1, 2, 3, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_empty_queue(self):
        method_names = ["MyQueue", "pop", "empty"]
        params = [[], [], []]
        expected_output = [None, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_pops(self):
        method_names = ["MyQueue", "push", "push", "pop", "pop", "pop", "empty"]
        params = [[], [1], [2], [], [], [], []]
        expected_output = [None, None, None, 1, 2, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_peek_without_pushes(self):
        method_names = ["MyQueue", "peek", "empty"]
        params = [[], [], []]
        expected_output = [None, None, True]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
    
    def test_peeks(self):
        method_names = ["MyQueue", "push", "push", "peek", "pop", "peek", "empty"]
        params = [[], [1], [2], [], [], [], []]
        expected_output =[None, None, None, 1, 1, 2, False]
        actual_output = self.helper.run_methods(method_names, params)
        self.assertEqual(actual_output, expected_output)
        
#######################################
if __name__ == '__main__':
    unittest.main()





