from collections import deque, Counter
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Count the occurrences of each task
        task_count = Counter(tasks)

        # Create a max heap to store the remaining count of tasks
        max_heap = []
        for cnt in task_count.values():
            heappush(max_heap, -cnt)

        # Initialize the time counter
        time = 0

        # Create a deque to store tasks in their cooldown period
        waiting_q = deque([])

        # Continue the loop until both max_heap and waiting_q are empty (all tasks executed)
        while max_heap or waiting_q:
            # Increment the time counter
            time += 1

            # If there are tasks left in the max_heap, process the highest count task
            if max_heap:
                count = -heappop(max_heap)
                # If the task still has remaining count, add it to waiting_q with its cooldown timestamp
                if count - 1 > 0:
                    waiting_q.append((count - 1, time + n))

            # If there are tasks in waiting_q, check if their cooldown has passed
            if waiting_q:
                count, cooldown_time = waiting_q[0]
                # If the cooldown has passed, add the task back to the max_heap for scheduling
                if cooldown_time == time:
                    heappush(max_heap, -count)
                    waiting_q.popleft()

        # Return the total time taken to complete all tasks
        return time
