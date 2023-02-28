import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_981_solution import TimeMap
from helpers.leetcode_981_helper import Helper

class Test(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()

    def test_example_1(self):
        params = (
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
        )
        expected_output = [None, None, "bar", "bar", None, "bar2", "bar2"]

        actual_output = self.helper.execute_methods(TimeMap(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = (
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 3]]
        )
        expected_output = [None, None, "bar", "bar", None, "bar2", "bar"]

        actual_output = self.helper.execute_methods(TimeMap(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_outbound_low(self):
        params = (
            ["TimeMap","set","set","get","get","get","get","get"],
            [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        )
        expected_output = [None,None,None,"","high","high","low","low"]

        actual_output = self.helper.execute_methods(TimeMap(), *params)
        self.assertEqual(actual_output, expected_output)

    def test_key_not_found(self):
        params = (
            ["TimeMap","set","set","get","set","get","get"],
            [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
        )
        expected_output = [None,None,None,"",None,"bar2","bar2"]

        actual_output = self.helper.execute_methods(TimeMap(), *params)
        self.assertEqual(actual_output, expected_output)

######################################
if __name__ == '__main__':
    unittest.main()
