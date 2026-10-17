class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        # dynamic programming solution
        for i in range(len(cost) -1, -1, -1):
            s1 = dp[i + 1] + cost[i]
            s2 = dp[i + 2] + cost[i] if (i + 2) <= len(cost) else float('inf')
            dp[i] = min(s1, s2)
        return min(dp[0], dp[1])
            

