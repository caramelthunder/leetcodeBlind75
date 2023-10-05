import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_247_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 2
        expected_output = ["11","69","88","96"]

        actual_output = self.solution.findStrobogrammatic(n)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        n = 1
        expected_output = ["0","1","8"]

        actual_output = self.solution.findStrobogrammatic(n)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_example_3(self):
        n = 4
        expected_output = ["1001","1111","1691","1881",
                           "1961","6009","6119","6699",
                           "6889","6969","8008","8118",
                           "8698","8888","8968","9006",
                           "9116","9696","9886","9966"]

        actual_output = self.solution.findStrobogrammatic(n)
        self.assertCountEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()
