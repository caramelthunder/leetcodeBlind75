
class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        # Sort the costs by savings (if we chose to go with City A. costB - costA).
        costs_by_savings = sorted(costs, key= lambda x: x[1] - x[0], reverse= True)
        minimum_total_cost = 0
        
        for i in range(n):
            # Assign the first n//2 people to city A and the rest to city B
            city = int(i >= n // 2)
            minimum_total_cost += costs_by_savings[i][city]

        return minimum_total_cost