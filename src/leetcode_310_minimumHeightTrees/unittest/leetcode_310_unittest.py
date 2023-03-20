import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_310_using_queue import Solution as Solution1
from solutions.leetcode_310_using_stack import Solution as Solution2

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        n, edges = 4, [[1,0],[1,2],[1,3]]
        expected_output = [1]

        actual_output = self.solution1.findMinHeightTrees(n, edges)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.findMinHeightTrees(n, edges)
        self.assertCountEqual(actual_output, expected_output)
    
    def test_example_2(self):
        n, edges = 6, [[3,0],[3,1],[3,2],[3,4],[5,4]]
        expected_output = [3,4]

        actual_output = self.solution1.findMinHeightTrees(n, edges)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.findMinHeightTrees(n, edges)
        self.assertCountEqual(actual_output, expected_output)




######################################
if __name__ == '__main__':
    unittest.main()