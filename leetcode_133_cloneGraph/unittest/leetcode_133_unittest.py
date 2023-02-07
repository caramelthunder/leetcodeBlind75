import sys
import os
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.leetcode_133_helper import GraphHelper
from solutions.leetcode_133_breadth_first import Solution as BFS
from solutions.leetcode_133_depth_first import Solution as DFS

class Test(unittest.TestCase):
    def setUp(self):
        self.graphHelper = GraphHelper()
        self.bfs = BFS()
        self.dfs = DFS()
    
    def test_example_1(self):
        adjList = [[2,4],[1,3],[2,4],[1,3]]
        graph = self.graphHelper.adjLst_to_graph(adjList)
        expected_output = [[2,4],[1,3],[2,4],[1,3]]
        
        cloned_graph = self.bfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))

        cloned_graph = self.dfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))
    
    def test_example_2(self):
        adjList = [[]]
        graph = self.graphHelper.adjLst_to_graph(adjList)
        expected_output = [[]]
        
        cloned_graph = self.bfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))

        cloned_graph = self.dfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))
    
    def test_example_3(self):
        adjList = []
        graph = self.graphHelper.adjLst_to_graph(adjList)
        expected_output = []
        
        cloned_graph = self.bfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))

        cloned_graph = self.dfs.cloneGraph(graph)
        self.assertEqual(self.graphHelper.graph_to_adjLst(cloned_graph), expected_output)
        if graph and cloned_graph:
            self.assertFalse(id(graph) == id(cloned_graph))

#######################################
if __name__ == '__main__':
    unittest.main()
