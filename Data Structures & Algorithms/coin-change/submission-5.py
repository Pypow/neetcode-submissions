class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                diff = a - c
                if diff >= 0:
                    dp[a] = min(1 + dp[diff], dp[a])
        return dp[amount] if dp[amount] != (amount + 1) else -1

