import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_721_union_find import Solution as Solution1
from solutions.leetcode_721_depth_first import Solution as Solution2
from solutions.leetcode_721_breadth_first import Solution as Solution3


class Test(unittest.TestCase):
    def setUp(self):
        self.solution1 = Solution1()
        self.solution2 = Solution2()
        self.solution3 = Solution3()

    def test_example_1(self):
        accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
        expected_output = [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]

        actual_output = self.solution1.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution3.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)

    def test_example_2(self):
        accounts = [
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
        ]
        expected_output = [
            ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
            ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
            ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
        ]

        actual_output = self.solution1.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution2.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)

        actual_output = self.solution3.accountsMerge(accounts)
        self.assertCountEqual(actual_output, expected_output)



######################################
if __name__ == '__main__':
    unittest.main()