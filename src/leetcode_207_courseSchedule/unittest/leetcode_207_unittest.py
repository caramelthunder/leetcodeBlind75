import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_207_dfs_cycle_detection import Solution as Solution1
from solutions.leetcode_207_topological_order import Solution as Solution2

class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()

    def test_example_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected_output = True

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        expected_output = False

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)
    
    def test_simple_chain(self):
        numCourses = 3
        prerequisites = [[1, 0], [2, 1]]
        expected_output = True

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_dependencies(self):
        numCourses = 3
        prerequisites = [[0, 1], [0, 2], [1, 2]]
        expected_output = True

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_cycle(self):
        numCourses = 3
        prerequisites = [[0, 1], [1, 2], [2, 0]]
        expected_output = False

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_complex_dependencies(self):
        numCourses = 4
        prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
        expected_output = False

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        expected_output = True

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

    def test_no_dependencies(self):
        numCourses = 2
        prerequisites = []
        expected_output = True

        actual_output = self.solution1.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.canFinish(numCourses, prerequisites)
        self.assertEqual(actual_output, expected_output)

#######################################
if __name__ == '__main__':
    unittest.main()

