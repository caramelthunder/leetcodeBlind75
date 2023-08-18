from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if a person could attend all meetings without any overlaps.

        Args:
            intervals (List[List[int]]): A list of intervals where each interval is a list of two integers 
                                         representing the start and end time of a meeting.

        Returns:
            bool: True if a person can attend all meetings without overlap, False otherwise.

        Runtime and space complexity:
            Time(n): O(n log n) - due to sorting of intervals.
            Space(n): O(1) - constant space, in-place sort.
        """
        # Sort the intervals based on start times.
        intervals.sort(key=lambda x: x[0])
        
        # Check if there's any overlap between consecutive intervals.
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
