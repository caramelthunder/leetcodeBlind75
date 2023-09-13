import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_588_helper import FunctionHelper
from solutions.leetcode_588_solution import FileSystem as FileSystem
from solutions.leetcode_588_with_simple_cache import (
    FileSystem as SimpleCacheFileSystem,
)
from solutions.leetcode_588_with_complex_cache import (
    FileSystem as ComplexCacheFileSystem,
)


class Test(unittest.TestCase):
    def test_example_1(self):
        inputs = [
            [
                "FileSystem",
                "ls",
                "mkdir",
                "addContentToFile",
                "ls",
                "readContentFromFile",
            ],
            [
                [],
                ["/"],
                ["/a/b/c"],
                ["/a/b/c/d", "hello"],
                ["/"],
                ["/a/b/c/d"],
            ],
        ]
        expected_output = [None, [], None, None, ["a"], "hello"]

        actual_output = FunctionHelper(FileSystem()).execute_methods(*inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(
            SimpleCacheFileSystem()
        ).execute_methods(*inputs)
        self.assertEqual(actual_output, expected_output)

        actual_output = FunctionHelper(
            ComplexCacheFileSystem()
        ).execute_methods(*inputs)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == "__main__":
    unittest.main()
