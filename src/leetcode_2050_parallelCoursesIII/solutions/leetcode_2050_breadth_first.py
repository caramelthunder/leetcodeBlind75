from collections import deque

class Solution:
    '''
    BFS approach
    
    Time complexity: O(n + m)
    The time complexity is dominated by the traversal of the graph edges and vertices. 
    In the worst case, we will traverse all the relations (edges) and courses (vertices). 
    Hence, the time complexity is O(n + m).

    Space complexity: O(n + m)
    The space complexity is determined by the size of the prerequisite graph and in-degree count dictionary. 
    In the worst case, the graph will have n vertices and m edges, which gives us O(n + m) space complexity. 
    Additional space is used for the deque and lead_time dictionary, but they both have the same upper bound O(n).
    '''

    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        
        prereq_to_course, prereq_cnt = self._build_graph(n=n, edges= relations)
        ready_to_start = [course for course in prereq_cnt if prereq_cnt[course] == 0]
        lead_time = {course: 0 for course in range(1, n + 1)}

        ready_to_start = deque(ready_to_start)
        course_taken = 0
        _total_time = 0

        while ready_to_start:
            course = ready_to_start.popleft()
            course_taken += 1

            _complete_course_time = lead_time[course] + time[course - 1]

            for next_course in prereq_to_course[course]:
                lead_time[next_course] = max(lead_time[next_course], _complete_course_time)

                prereq_cnt[next_course] -= 1
                if prereq_cnt[next_course] == 0:
                    ready_to_start.append(next_course)

            _total_time = max(_total_time, _complete_course_time)

        return _total_time if course_taken == n else 0
    
    def _build_graph(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        in_degrees = {i: 0 for i in range(1, n + 1)}

        for a, b in edges:
            graph[a].append(b)
            in_degrees[b] += 1

        return (graph, in_degrees)
            