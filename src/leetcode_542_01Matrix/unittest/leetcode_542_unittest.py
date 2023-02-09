import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_542_two_passes import Solution as Solution1
from solutions.leetcode_542_using_queue import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_axample_0(self):
        mat = [
            [0,0,0,0,1],
            [0,0,0,0,0],
            [0,1,1,0,0],
            [1,1,1,1,0],
            [0,1,1,1,0]]
        expected_output = [
            [0,0,0,0,1],
            [0,0,0,0,0],
            [0,1,1,0,0],
            [1,2,2,1,0],
            [0,1,2,1,0]]

        actual_output1 = self.solution1.updateMatrix(mat)
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.solution2.updateMatrix(mat)
        self.assertEqual(actual_output2, expected_output)

    def test_axample_1(self):
        mat = [
            [0,0,0],
            [0,1,0],
            [0,0,0]]
        expected_output = [
            [0,0,0],
            [0,1,0],
            [0,0,0]]

        actual_output1 = self.solution1.updateMatrix(mat)
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.solution2.updateMatrix(mat)
        self.assertEqual(actual_output2, expected_output)
    
    def test_axample_2(self):
        mat = [
            [0,0,0],
            [0,1,0],
            [1,1,1]]
        expected_output = [
            [0,0,0],
            [0,1,0],
            [1,2,1]]

        actual_output1 = self.solution1.updateMatrix(mat)
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.solution2.updateMatrix(mat)
        self.assertEqual(actual_output2, expected_output)

    def test_larger_matrix(self):
        mat = [
            [1,0,1,1,0,0,1,0,0,1],
            [0,1,1,0,1,0,1,0,1,1],
            [0,0,1,0,1,0,0,1,0,0],
            [1,0,1,0,1,1,1,1,1,1],
            [0,1,0,1,1,0,0,0,0,1],
            [0,0,1,0,1,1,1,0,1,0],
            [0,1,0,1,0,1,0,0,1,1],
            [1,0,0,0,1,1,1,1,0,1],
            [1,1,1,1,1,1,1,0,1,0],
            [1,1,1,1,0,1,0,0,1,1]
            ]
        expected_output = [
            [1,0,1,1,0,0,1,0,0,1],
            [0,1,1,0,1,0,1,0,1,1],
            [0,0,1,0,1,0,0,1,0,0],
            [1,0,1,0,1,1,1,1,1,1],
            [0,1,0,1,1,0,0,0,0,1],
            [0,0,1,0,1,1,1,0,1,0],
            [0,1,0,1,0,1,0,0,1,1],
            [1,0,0,0,1,2,1,1,0,1],
            [2,1,1,1,1,2,1,0,1,0],
            [3,2,2,1,0,1,0,0,1,1]
            ]

        actual_output1 = self.solution1.updateMatrix(mat)
        self.assertEqual(actual_output1, expected_output)
        actual_output2 = self.solution2.updateMatrix(mat)
        self.assertEqual(actual_output2, expected_output)

###################################
if __name__ == '__main__':
    unittest.main()