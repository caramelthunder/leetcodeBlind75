import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.leetcode_252_solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_no_meetings(self):
        self.assertTrue(self.solution.canAttendMeetings([]))
    
    def test_single_meeting(self):
        self.assertTrue(self.solution.canAttendMeetings([[1, 5]]))
    
    def test_no_overlaps(self):
        intervals = [[1, 3], [3, 5], [5, 8], [9, 12]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))
    
    def test_overlap_at_start(self):
        intervals = [[1, 4], [3, 5], [6, 8]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))
    
    def test_overlap_at_end(self):
        intervals = [[1, 3], [4, 6], [5, 8]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))
    
    def test_sub_interval(self):
        intervals = [[1, 10], [3, 5]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))
    
    def test_multiple_overlaps(self):
        intervals = [[1, 3], [2, 6], [3, 5], [6, 8]]
        self.assertFalse(self.solution.canAttendMeetings(intervals))
    
    def test_continuous_intervals(self):
        intervals = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))
    
    def test_large_gaps(self):
        intervals = [[1, 2], [10, 15], [20, 25]]
        self.assertTrue(self.solution.canAttendMeetings(intervals))

######################################
if __name__ == "__main__":
    unittest.main()
