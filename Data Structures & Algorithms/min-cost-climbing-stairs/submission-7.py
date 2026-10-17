class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {len(cost): 0}     # i: cost -> from i top, whats the min cost
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]
        return min(dfs(0), dfs(1))  # can be started at 0 or 1