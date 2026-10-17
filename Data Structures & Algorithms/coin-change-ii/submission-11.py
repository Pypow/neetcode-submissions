class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}     # (i, amt): no of distinct ways
        def dfs(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]
            if amt == amount:
                return 1
            if i >= len(coins) or amt > amount:
                return 0

            ways = dfs(i, coins[i] + amt) + dfs(i + 1, amt)
            dp[(i, amt)] = ways
            return dp[(i, amt)]
        return dfs(0,0)