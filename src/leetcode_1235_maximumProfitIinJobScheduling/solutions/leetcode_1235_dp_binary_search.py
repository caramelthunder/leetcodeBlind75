from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Given a list of start times, end times, and profits for jobs, computes the maximum profit that can be
        obtained by scheduling the jobs such that no two jobs overlap.

        Args:
            startTime (List[int]): List of start times of jobs.
            endTime (List[int]): List of end times of jobs.
            profit (List[int]): List of profits for each job.

        Returns:
            int: The maximum profit obtainable without overlapping any jobs.

        Run Time Complexities:
            Time: O(n log n) due to sorting operation. The binary search in _job_search takes O(log n) time.
            Space: O(n) due to the 'jobs' list.
        """

        
        # Error handling for inconsistent input lengths
        if not (len(startTime) == len(endTime) == len(profit)):
            raise ValueError("Input lists have inconsistent lengths.")

        # Helper function to perform a binary search 
        # to find the last non-overlapping job before a given start time
        def _job_search(target_end_time, left, right):
            non_overlapping_index = -1
            while left <= right:
                mid = left + (right - left) // 2
                job = jobs[mid]
                if job[1] <= target_end_time:
                    non_overlapping_index = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return non_overlapping_index

        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job: job[1])  # Sort by job end_time

        max_profits = [job[2] for job in jobs]  # Separate list to store profits
        
        for i in range(1, len(jobs)):
            curr_start_time, _, curr_profit = jobs[i]
            non_overlapping_index = _job_search(curr_start_time, 0, i)
            
            last_profit = max_profits[non_overlapping_index] if non_overlapping_index >= 0 else 0
            max_profits[i] = max(max_profits[i - 1], last_profit + curr_profit)

        return max_profits[-1] if max_profits else 0  # Handling the case of empty jobs
