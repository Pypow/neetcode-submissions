class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = r + 1 
            if r >= len(prices):
                break
            profit = prices[r] - prices[l]
            if profit > 0:
                res = max(res, profit)
            r += 1
        return res
            
