from collections import deque

class UnionFind:
	def __init__(self, grid= None):
		self.groups_map = {}

		self.count = 0
		if grid:
			for row in range(len(grid)):
				for col in range(len(grid[0])):
					self.count += (grid[row][col] == '1')
	
	def find(self, x):
		group = self.groups_map.get(x, x)
		if group == x:
			self.groups_map[x] = group
		else:
			self.groups_map[x] = self.find(group)
		return self.groups_map[x]
	
	def union(self, x, y):
		group_x = self.find(x)
		group_y = self.find(y)
		if group_x != group_y:
			self.groups_map[y] = group_x
			self.count -= 1


	def get_groups_count(self):
		return self.count

class Solution:
	def numIslands(self, grid: list[list[str]]) -> int:
		if not grid:
			return 0

		R, C = len(grid), len(grid[0])
		uf = UnionFind(grid)

		for row in range(R):
			for col in range(C):
				if grid[row][col] == '1':
					self._numIslands(grid, uf, R, C, row, col)

		return uf.get_groups_count()

	def _numIslands(self, grid, uf, R, C, row, col):
		q = deque([(row, col)])
		grid[row][col] = '0'
		
		while q:
			row, col = q.popleft()

			for _r, _c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				new_row = _r + row
				new_col = _c + col
				if R > new_row >= 0 and C > new_col >= 0 and grid[new_row][new_col] == '1':
					grid[new_row][new_col]  = '0'
					uf.union((row, col), (new_row, new_col))
					q.append((new_row, new_col))