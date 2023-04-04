class Solution:
    '''
    DFS approach with memoization:

    Time complexity: O(n + m)
    In the worst case, the DFS algorithm will traverse all the relations (edges) and courses (vertices) in the graph, 
    resulting in O(n + m) time complexity. 
    The memoization helps to prevent redundant computations by caching results, 
    which also contributes to the overall O(n + m) time complexity.

    Space complexity: O(n + m)
    The space complexity is determined by the size of the prerequisite graph and out-degree count dictionary. 
    In the worst case, the graph will have n vertices and m edges, which gives us O(n + m) space complexity. 
    Additional space is used for the cache, function call stack (due to recursion), 
    and other variables, but they all have the same upper bound O(n).
    '''

    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        
        course_have_prereq, next_course_cnt = self._build_graph(n=n, edges= relations)
        final_courses = [course for course in next_course_cnt if next_course_cnt[course] == 0]
        cache = {}
        _total_time = 0

        for course in final_courses:
            _time_to_complete = self._minimumTime(course_have_prereq, time, course, cache)
            _total_time = max(_total_time, _time_to_complete)

        return _total_time
    
    def _minimumTime(self, course_have_prereq, time, course, cache= {}):
        if not course_have_prereq[course]:
            return time[course - 1]
        
        if course not in cache:
            
            _longest_prereq_complete_time = 0
            for prereq in course_have_prereq[course]:
                _prereq_complete_time = self._minimumTime(course_have_prereq, time, prereq, cache)
                _longest_prereq_complete_time = max(_longest_prereq_complete_time, _prereq_complete_time)
            
            _course_complete_time = _longest_prereq_complete_time + time[course - 1]
            cache[course] = _course_complete_time
            
        return cache[course]
    
    def _build_graph(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        out_degrees = {i: 0 for i in range(1, n + 1)}

        for a, b in edges:
            graph[b].append(a)
            out_degrees[a] += 1

        return (graph, out_degrees)
            