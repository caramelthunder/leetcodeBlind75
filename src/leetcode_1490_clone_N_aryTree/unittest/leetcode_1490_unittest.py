import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_1490_iterative import Solution as IterativeSolution
from solutions.leetcode_1490_recursive import Solution as RecursiveSolution
from helpers.leetcode_1490_helper import TreeHelpers


class Test(unittest.TestCase):
    def setUp(self):
        self.iterative_clone_tree = IterativeSolution().cloneTree
        self.recursive_clone_tree = RecursiveSolution().cloneTree
        self.dict_to_tree = TreeHelpers().dict_to_tree
        self.tree_to_dict = TreeHelpers().tree_to_dict

    def test_01(self):
        root = self.dict_to_tree(1, {1: [3, 2, 4], 3: [5, 6]})
        expected_output = {1: [3, 2, 4], 3: [5, 6]}

        cloned_root = self.iterative_clone_tree(root)
        self.assertEqual(self.tree_to_dict(cloned_root), expected_output)
        self.assertNotEqual(id(cloned_root), id(root))

        cloned_root = self.recursive_clone_tree(root)
        self.assertEqual(self.tree_to_dict(cloned_root), expected_output)
        self.assertNotEqual(id(cloned_root), id(root))

    def test_02(self):
        root = self.dict_to_tree(
            1,
            {
                1: [2, 3, 4, 5],
                3: [6, 7],
                4: [8],
                5: [9, 10],
                7: [11],
                8: [12],
                9: [13],
                11: [14],
            },
        )

        expected_output = {
            1: [2, 3, 4, 5],
            3: [6, 7],
            4: [8],
            5: [9, 10],
            7: [11],
            8: [12],
            9: [13],
            11: [14],
        }

        cloned_root = self.iterative_clone_tree(root)
        self.assertEqual(self.tree_to_dict(cloned_root), expected_output)
        self.assertNotEqual(id(cloned_root), id(root))

        cloned_root = self.recursive_clone_tree(root)
        self.assertEqual(self.tree_to_dict(cloned_root), expected_output)
        self.assertNotEqual(id(cloned_root), id(root))


######################################
if __name__ == "__main__":
    unittest.main()
