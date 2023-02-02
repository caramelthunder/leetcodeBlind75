
import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_121_solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        input_prices = [7,1,5,3,6,4]
        expected_output = 5

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)

    def test_example2(self):
        input_prices = [7,6,4,3,1]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
        
    def test_increasing_prices(self):
        input_prices = [1,2,3,4,5,6,7]
        expected_output = 6

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
    def test_decreasing_prices(self):
        input_prices = [7,6,5,4,3,2,1]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)
        
    def test_single_day(self):
        input_prices = [7]
        expected_output = 0

        output = self.s.main(input_prices)
        self.assertEqual(output, expected_output)

##################################
if __name__ == '__main__':
    unittest.main()