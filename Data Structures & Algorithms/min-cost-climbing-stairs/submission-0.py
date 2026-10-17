class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i, exp):
            if i >= len(cost):
                return exp

            exp1 = dfs(i+1, exp + cost[i+1]) if (i+1) < len(cost) else exp
            exp2 = dfs(i+2, exp + cost[i+2]) if (i+2) < len(cost) else exp
        
            return min(exp1, exp2)
        
        return min(dfs(0, cost[0]), dfs(1, cost[1]))
            