import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_877_solution import Solution


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        piles = [5,3,4,5]
        expected_output = True

        actual_output = self.solution.stoneGame(piles)
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        piles = [3,7,2,3]
        expected_output = True

        actual_output = self.solution.stoneGame(piles)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()

'''
Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example 2:
Input: piles = [3,7,2,3]
Output: true
'''