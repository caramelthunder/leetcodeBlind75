import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_973_using_sort import Solution as Solution1
from solutions.leetcode_973_using_heap import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
    
    def test_example_1(self):
        points, k = [[1,3],[-2,2]], 1
        expected_output = [[-2,2]]

        actual_output = self.solution1.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        points, k = [[3,3],[5,-1],[-2,4]], 2
        expected_output = [[3,3],[-2,4]]

        actual_output = self.solution1.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_3(self):
        points, k = [[0,0],[1,1],[2,2]], 2
        expected_output = [[0,0],[1,1]]

        actual_output = self.solution1.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_4(self):
        points, k = [[1,3],[-2,2],[0,0],[5,5],[10,10],[-10,-10]], 3
        expected_output = [[0,0],[-2,2],[1,3]]

        actual_output = self.solution1.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_5(self):
        points, k = [[-10,-10],[10,10],[5,5],[0,0],[-2,2],[1,3]], 3
        expected_output = [[0,0],[-2,2],[1,3]]

        actual_output = self.solution1.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.kClosest(points, k)
        self.assertCountEqual(actual_output, expected_output)

#####################################
if __name__ == '__main__':
    unittest.main()

