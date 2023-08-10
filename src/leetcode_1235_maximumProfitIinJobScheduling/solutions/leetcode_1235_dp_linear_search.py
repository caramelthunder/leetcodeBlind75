from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """Computes the maximum profit by scheduling jobs without overlapping.

        This function calculates the maximum profit that can be achieved by scheduling
        jobs without any time overlaps. It uses the greedy algorithm and linear search
        to achieve this.

        Args:
            startTime (List[int]): List of start times for each job.
            endTime (List[int]): List of end times for each job.
            profit (List[int]): List of profits for each job.

        Returns:
            int: The maximum profit obtainable without overlapping any jobs.

        Run Time Complexities:
            Time: O(n^2) - primarily due to the linear search in _job_search for each job.
            Space: O(n) - due to the 'jobs' list.
        """
        # Error handling for inconsistent input lengths
        if not (len(startTime) == len(endTime) == len(profit)):
            raise ValueError("Input lists have inconsistent lengths.")
        
        # Helper function to perform a linear search 
        # to find the last non-overlapping job before a given start time
        def _job_search(target_end_time, left, right):
            i = right - 1
            while left <= i:
                job = jobs[i]
                if job[1] <= target_end_time:
                    return i
                i -= 1
            return -1

        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job: job[1])  # Sort by job end_time

        max_profits = [job[2] for job in jobs]  # Separate list to store profits

        for i in range(1, len(jobs)):
            curr_start_time, _, profit = jobs[i]
            last_non_overlap_job = _job_search(curr_start_time, 0, i)

            last_profit = max_profits[last_non_overlap_job] if last_non_overlap_job >= 0 else 0
            max_profits[i] = max(max_profits[i - 1], last_profit + profit)

        return max_profits[-1] if max_profits else 0  # Handling the case of empty jobs
