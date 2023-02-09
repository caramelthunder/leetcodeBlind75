class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        merged_intervals = []
        i = 0
        # add all intervals starting before newInterval.
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1
        # add newInterval.
        merged_intervals.append(newInterval)
        # start processing the remainder intervals.
        while i < len(intervals):
            oldInterval = merged_intervals[-1]
            newInterval = intervals[i]
            if oldInterval[1] >= newInterval[0]:
                merged_intervals[-1] = self.merge(oldInterval, newInterval)
            else:
                merged_intervals.append(newInterval)
            i += 1
            
        return merged_intervals

    def merge(self, old, new):
        start = min(old[0], new[0])
        end = max(old[1], new[1])
        return [start, end]
