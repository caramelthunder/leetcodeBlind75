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

        for i in range(1, len(jobs)):
            curr_start_time, curr_end_time, profit = jobs[i]
            last_non_overlap_job = (0, 0, 0)

            if (res := _job_search(curr_start_time, 0, i)) >= 0:
                last_non_overlap_job = jobs[res]

            max_profit = max(jobs[i - 1][2], last_non_overlap_job[2] + profit)
            jobs[i] = (curr_start_time, curr_end_time, max_profit)

        return jobs[-1][2]
