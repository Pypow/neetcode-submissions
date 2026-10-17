class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}         # amt: min no of coins that sum to amt

        def dfs(amt):
            if amt in dp:
                return dp[amt]
            res = float('inf')
            for c in coins:
                if (amt - c) >= 0:             # filter impossible values
                    res = min(res, 1 + dfs(amt - c))    
            dp[amt] = res
            return res
        coin = dfs(amount)
        return -1 if coin == float('inf') else coin

