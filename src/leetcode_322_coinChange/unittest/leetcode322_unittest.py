import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_322_top_down_memoisation import Solution as Solution1
from solutions.leetcode_322_bottom_up_tabulation import Solution as Solution2
from solutions.leetcode_322_bottom_up_bfs import Solution as Solution3

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()
    
    def test_example_1(self):
        coins, amount = [1,2,5], 11
        expected_output = 3

        actual_output = self.solution1.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        coins, amount = [2], 3
        expected_output = -1

        actual_output = self.solution1.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        coins, amount = [1], 0
        expected_output = 0

        actual_output = self.solution1.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_4(self):
        coins, amount = [1,2,5,10], 18
        expected_output = 4

        actual_output = self.solution1.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.coinChange(coins, amount)
        self.assertEqual(actual_output, expected_output)

#####################################
if __name__ == '__main__':
    unittest.main()
