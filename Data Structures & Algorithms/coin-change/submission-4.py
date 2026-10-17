class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if (a - c) >= 0:
                    tmp = 1 + dp[a - c]
                    dp[a] = min(dp[a], tmp)
        return dp[amount] if dp[amount] != (amount + 1) else -1