class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x: x[0])

        _merge = lambda a,b: [min(a[0], b[0]), max(a[1], b[1])]

        merged_intervals = []
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                new_interval = _merge(merged_intervals.pop(), interval)
                merged_intervals.append(new_interval)

        return merged_intervals