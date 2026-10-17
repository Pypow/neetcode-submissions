class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}
        def backtrack(num):
            if num in dp:
                return dp[num]
            sol = backtrack(num - 1) + backtrack(num - 2)
            dp[num] = sol
            return sol
        return backtrack(n)