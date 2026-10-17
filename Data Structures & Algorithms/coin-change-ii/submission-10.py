class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}         # (i, rem): no of ways

        def dfs(i, rem):
            if rem == 0:
                return 1
            if i >= len(coins):
                return 0
            if  rem < 0:
                return 0
            if (i, rem) in dp:
                return dp[(i, rem)]
            ways = dfs(i, rem - coins[i]) + dfs(i + 1, rem)
            dp[(i, rem)] = ways
            return ways
        return dfs(0, amount)