from typing import List
from dataclasses import dataclass


@dataclass
class Job:
    start_time: int = 0
    end_time: int = 0
    profit: int = 0


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

        # Perform a binary search to find the last non-overlapping job before a given start time.
        def _job_search(target_end_time: int, left: int, right: int) -> int:
            res = -1
            while left <= right:
                mid = left + (right - left) // 2
                job = jobs[mid]
                if job.end_time <= target_end_time:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        jobs = [Job(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job: job.end_time)  # Sort by job end_time

        for i in range(1, len(jobs)):
            curr_job = jobs[i]

            last_non_overlap_job = Job()
            if (res := _job_search(curr_job.start_time, 0, i)) >= 0:
                last_non_overlap_job = jobs[res]

            curr_job.profit = max(
                jobs[i - 1].profit,
                last_non_overlap_job.profit + curr_job.profit,
            )

        return jobs[-1].profit
