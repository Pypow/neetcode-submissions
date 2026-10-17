class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}     # (i, buying): max profit so far

        def dfs(i, buying):
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if i >= len(prices):
                return 0
            
            profit = 0
            if buying:
                profit = max(dfs(i + 1, not buying) - prices[i], 
                            dfs(i + 1, buying))
            
            else:
                profit = max(dfs(i + 2, not buying) + prices[i], 
                            dfs(i + 1, buying))
            dp[(i, buying)] = profit
            return dp[(i, buying)]
        return dfs(0, True)
        

