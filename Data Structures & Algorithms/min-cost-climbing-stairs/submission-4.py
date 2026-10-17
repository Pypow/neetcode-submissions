class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]

            s1 = dfs(i + 1) + cost[i]
            s2 = dfs(i + 2) + cost[i] if (i + 2) <= len(cost) else float('inf')
            dp[i] = min(s1, s2)
            return dp[i]
        return min(dfs(0), dfs(1))

