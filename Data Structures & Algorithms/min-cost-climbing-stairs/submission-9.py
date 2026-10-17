class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        goal = [float("inf")] * (len(cost) + 2)
        goal[len(cost)] = goal[len(cost) + 1] = 0                 
        for i in range(len(cost) - 1, -1, -1):
            curCost = cost[i] + min(goal[i + 1], goal[i + 2])   
            if goal[i] > curCost:
                goal[i] = curCost
        return min(goal[0], goal[1])         

