class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def minCost(i):
            total = cost[i]
            while (i + 1 < len(cost)) and (i + 2 < len(cost)):
                i = (i + 1) if cost[i+1] < cost[i+2] else (i + 2)
                total += cost[i]
            return total
        return min(minCost(0), minCost(1))