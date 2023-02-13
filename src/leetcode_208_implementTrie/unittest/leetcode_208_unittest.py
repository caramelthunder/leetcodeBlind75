import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_208_solution import Trie
from helpers.leetcode_208_helper import Helper

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
    
    def test_example_1(self):
        params = (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        )
        expected_output = [None, None, True, False, True, None, True]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"], ["append"], ["append"]]
        )
        expected_output = [None, None, True, False, True, None, True, None, True]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_empty_trie(self):
        params = (
            ["Trie", "search", "startsWith"],
            [[], ["apple"], ["app"]]
        )
        expected_output = [None, False, False]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_insert_existing_word(self):
        params = (
            ["Trie", "insert", "search", "insert", "search", "search"],
            [[], ["apple"], ["apple"], ["apple"], ["apple"], ["app"]]
        )
        expected_output = [None, None, True, None, True, False]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_insert_and_search_long_word(self):
        params = (
            ["Trie", "insert", "search"],
            [[], ["a" * 2000], ["a" * 2000]]
        )
        expected_output = [None, None, True]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_insert_and_search_long_prefix(self):
        params = (
            ["Trie", "insert", "startsWith", "startsWith"],
            [[], ["apple"], ["a" * 1999 + "p"], ["p" + "a" * 1999]]
        )
        expected_output = [None, None, False, False]
        actual_output = self.helper.execute_methods(Trie(), *params)
        self.assertEqual(actual_output, expected_output)


##########################################
if __name__ == '__main__':
    unittest.main()

