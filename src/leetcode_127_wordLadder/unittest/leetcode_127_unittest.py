import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_127_solution import Solution as Solution1

class Test(unittest.TestCase):

    def setUp(self):
        self.sol1 = Solution1()
    
    def test_example_1(self):
        params = {
            'beginWord': "hit", 
            'endWord': "cog", 
            'wordList': ["hot","dot","dog","lot","log","cog"]
        }
        expected_output = 5

        actual_output = self.sol1.ladderLength(**params)
        self.assertEqual(actual_output, expected_output)

    def test_example_2(self):
        params = {
            'beginWord': "hit", 
            'endWord': "cog", 
            'wordList': ["hot","dot","dog","lot","log"]
        }
        expected_output = 0

        actual_output = self.sol1.ladderLength(**params)
        self.assertEqual(actual_output, expected_output)


######################################
if __name__ == '__main__':
    unittest.main()