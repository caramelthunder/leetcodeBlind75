from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        in_degrees = self.get_in_degrees(graph, numCourses)
        q = deque([course for course in in_degrees if in_degrees[course] == 0])
        
        course_taken = 0

        while q:
            course = q.popleft()
            course_taken += 1

            for prereq in graph[course]:
                in_degrees[prereq] -= 1
                if in_degrees[prereq] == 0:
                    q.append(prereq)
        return course_taken == numCourses

    def get_in_degrees(self, graph, n):
        in_degrees = {node: 0 for node in range(n)}
        for node in in_degrees:
            for key in graph:
                if node in graph.get(key, []):
                    in_degrees[node] += 1
        return in_degrees

    def build_graph(self, n, adjLst):
        graph = {src: [] for src in range(n)}
        for dst, src in adjLst:
            graph[src].append(dst)
        return graph