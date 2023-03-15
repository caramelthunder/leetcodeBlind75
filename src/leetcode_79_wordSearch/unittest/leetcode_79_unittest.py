import sys
import os
import unittest
import copy

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_79_dfs_hashset import Solution as Solution1
from solutions.leetcode_79_dfs_space_optimized import Solution as Solution2
from solutions.leetcode_79_dfs_using_trie import Solution as Solution3

class Test(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_example_1(self):
        inputs = (
            [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]],
            "ABCCED"
        )
        expected_output = True

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_2(self):
        inputs = (
            [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            "SEE"
        )
        expected_output = True

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_3(self):
        inputs = (
            [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            "ABCB"
        )
        expected_output = False

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

    def test_example_4(self):
        inputs = (
            [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
            "SEE"
        )
        expected_output = True

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

    def test_example_5(self):
        inputs = (
            [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
            "ABCESEEEFS"
        )
        expected_output = True

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_6(self):
        inputs = (
            [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
            "ABCB"
        )
        expected_output = False

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)
    
    def test_example_7(self):
        inputs = (
            [["A"]],
            "A"
        )
        expected_output = True

        actual_output = self.solution1.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution2.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)

        actual_output = self.solution3.exist(*copy.deepcopy(inputs))
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()