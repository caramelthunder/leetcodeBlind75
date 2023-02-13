
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        visited = set()
        visiting = set()

        for course in range(numCourses):
            if not self._canFinish(graph, course, visiting, visited):
                return False
        return len(visited) == numCourses

    def _canFinish(self, graph, course, visiting, visited):
        if course in visited:
            return True
            
        # Encoutered a unfinished course, cycle-detected.
        if course in visiting:
            return False

        visiting.add(course)

        for prereq in graph[course]:
            if not self._canFinish(graph, prereq, visiting, visited):
                return False

        visiting.remove(course)
        visited.add(course)
        return True

    def build_graph(self, n, adjLst):
        graph = {src: [] for src in range(n)}
        for dst, src in adjLst:
            graph[src].append(dst)
        return graph